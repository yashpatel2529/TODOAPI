import email
from unicodedata import category
from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100)
    due_date =models.DateField()

    def __str__(self):
        return self.title

class Register (models.Model):
    email= models.EmailField(max_length=100)
    password= models.CharField(max_length=10)
