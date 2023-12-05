from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
