from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
  first_name=models.CharField(max_length=255)
  last_name=models.CharField(max_length=255)
  email = models.EmailField(unique=True)

  REQUIRED_FIELDS=['first_name','last_name','email']
