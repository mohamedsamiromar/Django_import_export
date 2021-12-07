from django.shortcuts import render
import pandas as pd
import logging
from project.row import check_row
from .models import Person
from .store_data import save_obj

logging.basicConfig(filename='person_log.log', level=logging.DEBUG)


def Import_file(request):
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

                if check_row(row, index):
                    invalid_row += 1

                else:

                    valid_row += 1
                    save_obj(row)

            logging.debug(('Valid Row : {}'.format(valid_row), 'Invalid Row: {}'.format(invalid_row)))
            return render(request, 'messages.html', {"messages": "Success"})
    return render(request, 'input.html')

