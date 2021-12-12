from django.urls import path, include
from project.views import Import_excel_file
from project.update_row_from_excel_file import update_email_excel_file


urlpatterns =[
    path('upload_excel', Import_excel_file, name='upload_file'),
    path('update_excel', update_email_excel_file)

]