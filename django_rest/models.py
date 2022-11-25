from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
from django.utils import timezone

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


class Todos(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(null=True, blank=True)
    due = models.DateTimeField(default=timezone.now)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}, by {self.user}, checked: {self.completed}"
