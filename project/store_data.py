from .models import Person


def save_obj(row):
    Person.objects.create(first_name=row.first_name, last_name=row.last_name, email=row.email)
    return save_obj
