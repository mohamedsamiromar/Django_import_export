from django.shortcuts import render
import pandas as pd
import logging
from project.row import check_row
from .models import Person
from .store_data import save_obj

logging.basicConfig(filename='person_log.log', level=logging.DEBUG)


def Import_excel_file(request):
    if request.method == 'POST':
        myfile = request.FILES['file']
        if myfile is None:
            return render(request, "messages.html", {"message": "Please, Upload Your File"})

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
