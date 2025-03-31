from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Rating


# Create your views here.
from .models import Contact

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def menu(request):
    return render(request, 'menu.html')

# def login(request):
#      return render(request, 'login.html')
def rate_us(request):
    return render(request, 'rate_us.html')
def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        category=request.POST.get('category')
        
        contact = Contact(name=name, phone=phone, message=message ,category=category,)
        
        contact.save()
        messages.success(request, "Your message has been sent!")
    return render(request, 'contact.html')

# views.py
def submit_rating(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        rating = request.POST.get('rating')
        comments = request.POST.get('comments')

        Rating.objects.create(
            name=name,
            rating=int(rating),
            comments=comments
        )
        return redirect('thank_you')

    return render(request, 'index.html')

def thank_you(request):
    return render(request, 'thank_you.html')


# def contact_form(request):
#     if request.method == 'post':
#         name=request.POST.get('name')
#         phone=request.POST.get('phone')
#         message=request.POST.get('message')
#         savedetails = contact(name=name , phone=phone, message=message)
#         savedetails.save()
#     return render(request, 'contact.html')
#
# # def contact(request):

# views.py

from django.contrib.auth import authenticate, login

# def signin(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#
#         if user is not None:
#             login(request, user)
#             return redirect('home')  # Replace 'home' with your actual home URL
#         else:
#             # Handle invalid login credentials
#             pass
#
#     return render(request, 'login.html')  # Create a template for the sign-in page
#
