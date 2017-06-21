from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Usernames(models.Model):
    username = models.CharField(max_length = 30)
    created_at = models.DateTimeField(auto_now_add = True)
    upated_at = models.DateTimeField(auto_now_add=True)