from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Person, ReadUpdate


@admin.register(Person)
class PersonAdmin(ImportExportModelAdmin):
    pass


@admin.register(ReadUpdate)
class ReadUpdateAdmin(ImportExportModelAdmin):
    pass
