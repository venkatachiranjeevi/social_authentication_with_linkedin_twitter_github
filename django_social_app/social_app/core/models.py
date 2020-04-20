import uuid

from django.db import models


class CustomUser(models.Model):
    id=models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4, primary_key=True)
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    username = models.CharField(max_length=255, blank=False)
    mobile_number = models.CharField(max_length=255, blank=True)
    meta_data = models.TextField(blank=True)
