from datetime import datetime

from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(blank=True, unique=True)
    job_title = models.CharField(max_length=150, null=True)
    country = models.CharField(max_length=30, null=True)
    city = models.CharField(max_length=75, null=True)
    created_by = models.CharField(max_length=30, default='system')
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_by = models.CharField(max_length=30, default='system')
    updated_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)


class ReadUpdate(models.Model):
    sku = models.CharField(max_length=750, null=True, unique=True)
    image_links = models.CharField(max_length=1500, null=True)
    attachment_links = models.CharField(max_length=1500, null=True)
