from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models.functions import TruncDate
from django.db.models import Count
from dabeli.models import Contact
import json

# Check if the user is a superuser
def is_superuser(user):
    return user.is_superuser

# Login View
def owner_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:  # Only allow superuser to log in
            login(request, user)
            return redirect('custom_admin_dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials or not a superuser.'})
    return render(request, 'login.html')

# Logout View
@login_required
def owner_logout(request):
    logout(request)
    return redirect('Home')

# Dashboard View (Restricted to superusers)
@login_required

def dashboard_view(request):
    try:
        # Fetch last 10 messages with all details
        messages = Contact.objects.all().order_by('-id')[:10]
        total_messages = Contact.objects.count()

        # Group messages by date (assuming `created_at` is a DateTimeField in Contact model)
        daily_messages = (
            Contact.objects
            .annotate(date=TruncDate('created_at'))  # Group by date
            .values('date')
            .annotate(count=Count('id'))
            .order_by('date')
        )

        # Prepare data for the daily messages chart
        days = [item['date'].strftime('%Y-%m-%d') for item in daily_messages]
        daily_counts = [item['count'] for item in daily_messages]  # Ensure counts are whole numbers

        # Example: Replace with actual message categories if applicable
        categories = ['General', 'Complaint', 'Suggestion']
        category_counts = [
            Contact.objects.filter(category='General').count(),
            Contact.objects.filter(category='Complaint').count(),
            Contact.objects.filter(category='Suggestion').count(),
        ]

        # Additional insights
        most_active_day = max(daily_messages, key=lambda x: x['count'])['date'].strftime('%Y-%m-%d') if daily_messages else "N/A"
        most_common_category = categories[category_counts.index(max(category_counts))] if category_counts else "N/A"
        avg_messages_per_day = total_messages / len(days) if len(days) > 0 else 0

    except Exception as e:
        messages = []
        total_messages = 0
        days, daily_counts, categories, category_counts = [], [], [], []
        most_active_day, most_common_category, avg_messages_per_day = "N/A", "N/A", 0
        print("Error fetching messages:", e)  # Debugging

    context = {
        "messages": messages,
        "total_messages": total_messages,
        "days": json.dumps(days),
        "daily_counts": json.dumps(daily_counts),
        "categories": json.dumps(categories),
        "category_counts": json.dumps(category_counts),
        "most_active_day": most_active_day,
        "most_common_category": most_common_category,
        "avg_messages_per_day": round(avg_messages_per_day, 2),
    }
    return render(request, "dashboard.html", context)

# Delete Message View
@login_required
@user_passes_test(is_superuser, login_url='owner_login')
def delete_message(request, message_id):
    message = get_object_or_404(Contact, id=message_id)
    message.delete()
    return redirect('dashboard_view')