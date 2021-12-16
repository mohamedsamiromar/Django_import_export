from django.urls import path
from .views import upload, listing

urlpatterns = [
    path('upload_file', upload, name='upload_file'),
    path('list_colums', listing, name='list_colums'),

]
