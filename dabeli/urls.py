"""
URL configuration for dukan project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from custom_admin.views import owner_login  # Import owner_login from custom_admin.views

urlpatterns = [
    path("", views.index, name="Home"),
    path("contact/", views.contact_form, name="contact"),
    path("about/", views.about, name="about"),
    path("menu/", views.menu, name="menu"),
    path("login/", owner_login, name="owner_login"),  # Use the correct import
    path("rate_us/", views.rate_us, name="rate_us"),
path('submit_rating/', views.submit_rating, name='submit_rating'),
    path('thank_you/', views.thank_you, name='thank_you'),
]



