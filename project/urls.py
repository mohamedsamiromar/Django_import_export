from django.urls import path, include
from project.views import Import_excel_file


urlpatterns =[
    path('upload_excel', Import_excel_file, name='upload_file'),

]