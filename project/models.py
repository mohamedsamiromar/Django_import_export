from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(blank=True, unique=True)
    country = models.CharField(max_length=30, null=True)
    city = models.CharField(max_length=75, null=True)
    created_by = models.CharField(max_length=30, default='system')
    created_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=30, default='system')
    updated_at = models.DateTimeField(auto_now=True)
