from django.shortcuts import render
from .models import Person
import pandas as pd
import logging

logging.basicConfig(filename='person_log.log', level=logging.DEBUG)


def Import_csv(request):
    if request.method == 'POST':
        myfile = request.FILES['file']

        file = str(myfile)
        if not file.endswith('xlsx') or file.endswith('xls'):
            return render(request, 'messages.html',
                          {'messages': 'The File Content Is Not As Expected'})
        else:
            df = pd.read_excel(myfile)
            invalid_row = 0
            valid_row = 0
            for index, row in df.iterrows():
                if pd.isna(row[0]):
                    invalid_row += 1
                    empty_row = ('Index: {}'.format(index), 'First Name: {}'.format(row.first_name),
                                 'Last Name: {}'.format(row.last_name), 'Email: {}'.format(row.email))
                    logging.debug(empty_row)
                    continue
                else:
                    valid_row += 1
                    Person.objects.create(first_name=row.first_name, last_name=row.last_name, email=row.email)
            logging.debug(('Valid Row : {}'.format(valid_row), 'Invalid Row: {}'.format(invalid_row)))
            return render(request, 'messages.html', {"messages": "Success"})
    return render(request, 'input.html')
