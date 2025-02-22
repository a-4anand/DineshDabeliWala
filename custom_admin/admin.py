from django.contrib import admin
from dabeli.models import Contact


# Check if Contact is already registered
if not admin.site.is_registered(Contact):
    admin.site.register(Contact)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'message')  # Fields to display in the admin panel
    search_fields = ('name', 'phone')  # Add search functionality
    list_filter = ('name',)  # Add filter options
