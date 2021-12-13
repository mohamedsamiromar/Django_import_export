from django.shortcuts import render
from django.utils.timezone import now

from .models import Person


def save_obj(row, request):
    check_email = Person.objects.filter(email=row.email)
    if check_email:
        return render(request, 'messages.html', {'mess'})
    Person.objects.create(first_name=row.first_name, last_name=row.last_name, email=row.email, created_at=now, job_title=row.job_title
                          , country=row.country, city=row.city)

    return save_obj
