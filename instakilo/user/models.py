from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class UserModel(AbstractUser):
    """created a class for user"""
    is_email_verified = models.BooleanField(default=False)
    
