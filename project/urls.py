from django.urls import path
from .views import upload
urlpatterns =[
    path('upload_file', upload, name='upload_file'),

]