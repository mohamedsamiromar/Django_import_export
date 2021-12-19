from django.urls import path
from .views import upload, listing

urlpatterns = [
    path('upload_file', upload, name='upload_file'),
    path('listing', listing, name='list_colums'),

]
