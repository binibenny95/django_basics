
from django.db import models

# Create your models here.

from datetime import datetime
from django.db import models
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(verbose_name='Category Title', max_length=255)

    def __str__(self):
        return self.title

class Note(models.Model):
    title = models.CharField(verbose_name='Note Title', max_length=255)
    text = models.TextField(verbose_name='Note Text', max_length=5000)
    reminder = models.TextField(verbose_name='Note Reminder', max_length=5000)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='notes')

    def __str__(self):
        return self.title

