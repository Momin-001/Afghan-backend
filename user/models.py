from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_super_admin = models.BooleanField(default=False)
    is_active =models.BooleanField(default=True)
    email=models.EmailField(unique=True)

    def __str__(self):
        return self.username
