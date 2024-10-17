from django.db import models

# Create your models here.

from datetime import datetime
from django.db import models
from django.utils import timezone

class Note(models.Model):
    title = models.CharField(verbose_name='Note Title', max_length=255)
    content = models.TextField(verbose_name='Note Content', max_length=255)
    date = models.DateField(verbose_name='Note Date', auto_now_add=True)

    def __str__(self):
        return self.title