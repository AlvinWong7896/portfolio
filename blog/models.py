from django.db import models
from django.utils import timezone


class Blog(models.Model):
    title = models.CharField(max_length=50)
    created_on = models.DateTimeField(default=timezone.now)
    message = models.TextField()
