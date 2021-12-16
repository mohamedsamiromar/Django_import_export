from datetime import datetime

from django.db import models


class ReadUpdate(models.Model):
    sku = models.CharField(max_length=150, null=True, unique=True)
    image_links = models.CharField(max_length=3072, null=True)
    attachment_links = models.CharField(max_length=3072, null=True)
