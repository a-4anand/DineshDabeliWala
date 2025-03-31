from django.db import models

# Create your models here.
# models.py

from django.contrib.auth.models import User



class Rating(models.Model):
    RATING_CHOICES = [
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    ]

    name = models.CharField(max_length=100, blank=True, null=True)
    rating = models.IntegerField(choices=RATING_CHOICES)
    comments = models.TextField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name if self.name else "Anonymous"} - {self.rating} Stars'


class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone=models.IntegerField(max_length=10,null=True)
    message = models.TextField()
    category = models.CharField(max_length=50, choices=[('General', 'General'), ('Complaint', 'Complaint'), ('Suggestion', 'Suggestion')],null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name




