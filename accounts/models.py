from django.contrib.auth.models import AbstractUser
from django.db import models

class Profile(AbstractUser):
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
