from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(default=datetime.date.today)
    EMAIL_FIELD = "username"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username
