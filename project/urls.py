from django.urls import path, include
from project.views import Import_file
from project.read import  try_view

urlpatterns =[
    path('upload_file', Import_file, name='upload_file'),
    path('upload', try_view, name='upload_file'),

]