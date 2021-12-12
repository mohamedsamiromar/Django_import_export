from django.urls import path, include
from CSV_data.csv_file import Import_csv_file
from CSV_data.update_emails_from_CSV_file import update_email_excel_file
urlpatterns =[
    path('upload_csv', Import_csv_file, name='upload_file'),
    path('update_csv', update_email_excel_file, name='update_csv')

]