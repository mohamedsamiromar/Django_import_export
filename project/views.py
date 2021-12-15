from django.shortcuts import render
import pandas as pd
import logging
from .models import Person, ReadUpdate
from .store_data import save_obj
from .update import update_row
logging.basicConfig(filename='person_log.log', level=logging.DEBUG)

'''
read data from file(excel, CSV) and create Django object from the data file 
'''


def Import_file(request):
    if request.method == 'POST':
        myfile = request.FILES['file']

        file = str(myfile)
        if file.endswith('xlsx') or file.endswith('xls'):  # check if file end with xlsx
            df = pd.read_excel(myfile, skiprows=' ')
        elif file.endswith('csv'):  # check if file end with csv
            df = pd.read_csv(myfile, skipinitialspace=True)
        else:  # if the file does not end with xlsx or csv will return this  message
            return render(request, 'messages.html',
                          {'messages': 'The File Content Is Not As Expected'})

        invalid_row = 0  # the counter will count the invalid row
        valid_row = 0  # the counter will count the valid row
        updated_row = 0  # the counter will count the updated row
        df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=True)  # Here will drop any empty row

        for index, row in df.iterrows():  # The loop reads the rows from the file

            # check if the row exists will update the row, if not exist will insert a row in the database
            try:
                get_row = ReadUpdate.objects.get(sku=row.sku)
            except ReadUpdate.DoesNotExist:
                get_row = None
            if get_row is None:

                save_obj(row)  # The function working to insert row in database

            else:
                update_row(get_row, row)  # The function working to update row
                updated_row += 1

        logging.debug(('Update Row : {}'.format(updated_row), 'Invalid Row: {}'.format(invalid_row)))
        logging.debug(('Valid Row : {}'.format(valid_row), 'Invalid Row: {}'.format(invalid_row)))
        return render(request, 'messages.html', {"messages": "Success"})
    return render(request, 'upload_excel_file.html')
