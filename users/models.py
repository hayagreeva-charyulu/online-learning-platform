from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('creator', 'Creator'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)


class Profile(models.Model):
    USER_TYPES = (
        ('student', 'Student'),
        ('creator', 'creator'),
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    role = models.CharField(max_length=10, choices=USER_TYPES, default='student')

    def __str__(self):
        return f"{self.user.username} Profile"

    
