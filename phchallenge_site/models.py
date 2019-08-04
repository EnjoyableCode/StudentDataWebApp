from django.db import models
from django.contrib.auth.models import User
import uuid


class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, null=True, blank=True)
    homepage_url = models.URLField()
    is_athlete = models.BooleanField(default=False)
    favorite_joke = models.CharField(max_length=500, null=True, blank=True)


