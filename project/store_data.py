from django.shortcuts import render
from django.utils.timezone import now

from .models import Person

'''
save_obj working to read the data from row and insert into database base
'''


def save_obj(row):
    Person.objects.create(first_name=row.first_name, last_name=row.last_name, email=row.email, created_at=now,
                          job_title=row.job_title, country=row.country, city=row.city)
    return save_obj
