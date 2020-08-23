from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
	content = models.CharField(max_length=128)
	owner = models.ForeignKey(User, related_name='todos', on_delete=models.CASCADE)