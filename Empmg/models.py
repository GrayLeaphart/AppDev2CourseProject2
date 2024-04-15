from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    role = models.CharField(max_length=100)

    class Meta:
        app_label = 'Empmg'
    

class Note(models.Model):
    heading = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.heading

