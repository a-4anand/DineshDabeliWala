from django.db import models

# Create your models here.
# models.py

from django.contrib.auth.models import User




class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone=models.IntegerField(max_length=10,null=True)
    message = models.TextField()
    category = models.CharField(max_length=50, choices=[('General', 'General'), ('Complaint', 'Complaint'), ('Suggestion', 'Suggestion')],null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name




