from django.urls import path, include
from project.views import Import_file

urlpatterns =[
    path('upload_file', Import_file, name='upload_file'),

]