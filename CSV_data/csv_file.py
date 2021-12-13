from django.shortcuts import render
import pandas as pd

from project.models import Person
from project.row import check_row
from project.store_data import save_obj
import logging


def Import_csv_file(request):
    if request.method == 'POST':
        myfile = request.FILES['file']

        file = str(myfile)

        if not file.endswith('csv'):
            return render(request, 'messages.html',
                          {'messages': 'The File Content Is Not As Expected'})
        else:
            invalid_row = 0
            valid_row = 0
            df = pd.read_csv(myfile)

            for index, row in df.iterrows():
                if check_row(row, index):
                    invalid_row += 1
                else:
                    valid_row += 1
                    try:
                        check_email = Person.objects.filter(email=row.email)
                        if check_email:
                            raise Exception("")
                    except:
                        return render(request, 'messages.html', {"messages": "Sorry,The File Have Duplicate Emails"})
                    else:
                        save_obj(row)

            logging.debug(('Valid Row : {}'.format(valid_row), 'Invalid Row: {}'.format(invalid_row)))
            return render(request, 'messages.html', {"messages": "Success"})
    return render(request, 'upload_excel_file.html')
