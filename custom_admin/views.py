from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models.functions import TruncDate
from django.db.models import Count
from dabeli.models import Contact, Rating
from django.views.decorators.csrf import csrf_exempt
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
@csrf_exempt
@login_required
@user_passes_test(is_superuser, login_url='owner_login')
def dashboard_view(request):
    try:
        # Fetch all messages with complete details
        messages = Contact.objects.all().order_by('-id')
        total_messages = messages.count()

        # Fetch all ratings with complete details
        ratings = Rating.objects.all().order_by('-submitted_at')
        total_ratings = ratings.count()
        avg_rating = round(sum(r.rating for r in ratings) / total_ratings, 2) if total_ratings > 0 else 0

        # Rating Distribution
        rating_counts = ratings.values('rating').annotate(count=Count('id')).order_by('rating')
        rating_labels = [f"⭐️ {item['rating']} Stars" for item in rating_counts]
        rating_data = [item['count'] for item in rating_counts]

        # Group messages by date
        daily_messages = (
            Contact.objects
            .annotate(date=TruncDate('created_at'))
            .values('date')
            .annotate(count=Count('id'))
            .order_by('date')
        )
        days = [item['date'].strftime('%Y-%m-%d') for item in daily_messages]
        daily_counts = [item['count'] for item in daily_messages]

        # Categories Information
        categories = ['General', 'Complaint', 'Suggestion']
        category_counts = [
            Contact.objects.filter(category='General').count(),
            Contact.objects.filter(category='Complaint').count(),
            Contact.objects.filter(category='Suggestion').count(),
        ]

        # Additional Insights
        most_active_day = max(daily_messages, key=lambda x: x['count'])['date'].strftime(
            '%Y-%m-%d') if daily_messages else "N/A"
        most_common_category = categories[category_counts.index(max(category_counts))] if category_counts else "N/A"
        avg_messages_per_day = round(total_messages / len(days), 2) if len(days) > 0 else 0

        # Additional Information for Messages and Ratings
        message_details = [
            {
                "id": msg.id,
                "name": msg.name,
                "phone": msg.phone,
                "category": msg.category,
                "message": msg.message,
                "created_at": msg.created_at.strftime('%Y-%m-%d %H:%M:%S') if msg.created_at else "N/A",
            }
            for msg in messages
        ]

        rating_details = [
            {
                "id": rating.id,
                "name": rating.name or "Anonymous",
                "rating": rating.rating,
                "comments": rating.comments or "No comments",
                "submitted_at": rating.submitted_at.strftime('%Y-%m-%d %H:%M:%S'),
            }
            for rating in ratings
        ]

    except Exception as e:
        messages, rating_labels, rating_data = [], [], []
        total_messages, total_ratings, avg_rating = 0, 0, 0
        days, daily_counts, categories, category_counts = [], [], [], []
        most_active_day, most_common_category, avg_messages_per_day = "N/A", "N/A", 0
        message_details, rating_details = [], []
        print("Error fetching messages or ratings:", e)

    context = {
        "messages": messages,
        "message_details": message_details,
        "total_messages": total_messages,
        "days": json.dumps(days),
        "daily_counts": json.dumps(daily_counts),
        "categories": json.dumps(categories),
        "category_counts": json.dumps(category_counts),
        "most_active_day": most_active_day,
        "most_common_category": most_common_category,
        "avg_messages_per_day": avg_messages_per_day,
        "total_ratings": total_ratings,
        "avg_rating": avg_rating,
        "rating_labels": json.dumps(rating_labels),
        "rating_data": json.dumps(rating_data),
        "rating_details": rating_details,
    }
    return render(request, "dashboard.html", context)


# Delete Message View
@login_required
@user_passes_test(is_superuser, login_url='owner_login')
def delete_message(request, message_id):
    message = get_object_or_404(Contact, id=message_id)
    if request.method == 'POST':
        message.delete()
        return redirect('custom_admin_dashboard')

    context = {
        "message": message,
    }
    return render(request, 'confirm_delete.html', context)
