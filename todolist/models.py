from django.db import models
from django.contrib.auth.models import User
from todolist.forms import TaskForm
import datetime

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    date = models.DateTimeField(auto_now_add = True)
    title = models.CharField(max_length = 100)
    description = models.TextField(default='')
