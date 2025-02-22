# custom_admin/urls.py

from django.urls import path
from custom_admin.views import dashboard_view
from custom_admin.views import delete_message,owner_login, owner_logout
from django.urls import path,include

urlpatterns = [
    path('login/',owner_login, name='owner_login'),  # Login page
    path('logout/',owner_logout, name='owner_logout'),  # Logout page
    path('dashboard/',dashboard_view, name='custom_admin_dashboard'),
    path('delete-message/<int:message_id>/', delete_message, name='delete_message'),
    path("",include('dabeli.urls'),name="Home"),
]


    # Define your custom admin URLs here

