from django.contrib import admin
#
from dabeli.models import Contact,Rating
#
#
#
# # Register your models here.
admin.site.register(Contact)
admin.site.register(Rating)

# your_app/admin.py

from django.contrib import admin

# Customize admin site behavior, e.g., change the site header
admin.site.site_header = 'Admin Dashboard'

# admin.py
# from django.contrib import admin

# class YourModelAdmin(admin.ModelAdmin):
#     class Media:
#         css = {
#             'all': ('path/to/admin_custom.css',),
#         }
