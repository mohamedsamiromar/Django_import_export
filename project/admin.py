from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import ReadUpdate


@admin.register(ReadUpdate)
class ReadUpdateAdmin(ImportExportModelAdmin):
    pass
