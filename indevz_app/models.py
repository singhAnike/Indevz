from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15)
    company_name = models.CharField(max_length=255)
    access_code = models.CharField(max_length=20, blank=True, null=True)
