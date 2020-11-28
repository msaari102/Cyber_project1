from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Account(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField()
    pii = models.TextField(default="12345")
    address = models.TextField(default="no-mans-land")

class Message(models.Model):
	source = models.ForeignKey(User, on_delete=models.CASCADE, related_name='source')
	target = models.ForeignKey(User, on_delete=models.CASCADE, related_name='target')
	content = models.TextField()
