from django.shortcuts import render
import pandas as pd
import logging
from project.row import check_row
from .models import Person
from .store_data import save_obj
from django.utils.timezone import now
from .update import update_row

logging.basicConfig(filename='person_log.log', level=logging.DEBUG)

'''
read data from file(excel, CSV) and create Django object from the data file 
'''


#
#
# def Import_file(request):
#     if request.method == 'POST':
#         myfile = request.FILES['file']
#
#         file = str(myfile)
#         if file.endswith('xlsx') or file.endswith('xls'):  # check if file end with xlsx
#             df = pd.read_excel(myfile)
#         elif file.endswith('csv'):  # check if file end with csv
#             df = pd.read_csv(myfile)
#         else:  # if the file does not end with xlsx or csv will return this  message
#             return render(request, 'messages.html',
#                           {'messages': 'The File Content Is Not As Expected'})
#
#         invalid_row = 0  # the counter will count the invalid row
#         valid_row = 0  # the counter will count the valid row
#         updated_row = 0  # the counter will count the updated row
#
#         for index, row in df.iterrows():  # The loop reads the rows from the file
#             if check_row(row, index):  # here will skip any empty row
#                 invalid_row += 1  # Add 1 to counter
#             else:
#                 valid_row += 1  # if file hasn't got any empty row will add 1 to counter
#                 try:
#                     get_email = Person.objects.get(email=row.email)
#                 except Person.DoesNotExist:
#                     get_email = None
#                 if get_email is None:
#                     save_obj(row)
#                 else:
#                     update_row(get_email, row)
#                     updated_row += 1
#                     logging.debug(('Valid Row : {}'.format(updated_row), 'Invalid Row: {}'.format(invalid_row)))
#                     return render(request, 'messages.html', {"messages": "Update Successes"})
#
#             logging.debug(('Valid Row : {}'.format(valid_row), 'Invalid Row: {}'.format(invalid_row)))
#             return render(request, 'messages.html', {"messages": "Success"})
#     return render(request, 'upload_excel_file.html')


def Import_file(request):
    if request.method == 'POST':
        myfile = request.FILES['file']
        if myfile is None:
            return render(request, "messages.html", {"message": "Please, Upload Your File"})

        file = str(myfile)
        if file.endswith('xlsx') or file.endswith('xls'):  # check if file end with xlsx
            df = pd.read_excel(myfile)
        elif file.endswith('csv'):  # check if file end with csv
            df = pd.read_csv(myfile)
        else:  # if the file does not end with xlsx or csv will return this  message
            return render(request, 'messages.html',
                          {'messages': 'The File Content Is Not As Expected'})

        invalid_row = 0  # the counter will count the invalid row
        valid_row = 0  # the counter will count the valid row
        updated_row = 0  # the counter will count the updated row

        for index, row in df.iterrows():  # The loop reads the rows from the file
            if check_row(row, index):  # here will skip any empty row
                invalid_row += 1  # Add 1 to counter if has invalid row
            else:
                valid_row += 1  # if file hasn't got any empty row will add 1 to counter

                # check if the row exists will update the row, if not exist will insert a row in the database
                try:
                    get_row = Person.objects.get(email=row.email)
                except Person.DoesNotExist:
                    get_row = None
                if get_row is None:

                    save_obj(row)  # The function working to insert row in database
                else:
                    update_row(get_row, row)  # The function working to update row
                    updated_row += 1
                    logging.debug(('Valid Row : {}'.format(updated_row), 'Invalid Row: {}'.format(invalid_row)))
        logging.debug(('Valid Row : {}'.format(valid_row), 'Invalid Row: {}'.format(invalid_row)))
        return render(request, 'messages.html', {"messages": "Success"})
    return render(request, 'upload_excel_file.html')
