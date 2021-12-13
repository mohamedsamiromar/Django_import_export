from django.shortcuts import render
import pandas as pd
import logging
from project.row import check_row
from .models import Person
from .store_data import save_obj
from django.utils.timezone import now

logging.basicConfig(filename='person_log.log', level=logging.DEBUG)


def Import_file(request):
    if request.method == 'POST':
        myfile = request.FILES['file']
        if myfile is None:
            return render(request, "messages.html", {"message": "Please, Upload Your File"})

        file = str(myfile)
        if file.endswith('xlsx') or file.endswith('xls'):
            df = pd.read_excel(myfile)
        elif file.endswith('csv'):
            df = pd.read_csv(myfile)
        else:
            return render(request, 'messages.html',
                          {'messages': 'The File Content Is Not As Expected'})

        invalid_row = 0
        valid_row = 0
        update_row = 0

        for index, row in df.iterrows():
            if check_row(row, index):
                invalid_row += 1
            else:
                valid_row += 1

                try:
                    get_row = Person.objects.get(email=row.email)
                except Person.DoesNotExist:
                    get_row = None
                if get_row is None:
                    try:
                        check_email = Person.objects.filter(email=row.email)
                        if check_email:
                            raise Exception("")
                    except:
                        return render(request, 'messages.html', {"messages": "Sorry,The File Have Duplicate Emails"})

                    save_obj(row)
                else:
                    get_row.country = row.country
                    get_row.city = row.city
                    get_row.job_title = row.job_title
                    get_row.created_at = now()
                    get_row.save()
                    update_row += 1

        logging.debug(('Valid Row : {}'.format(valid_row), 'Invalid Row: {}'.format(invalid_row)))
        return render(request, 'messages.html', {"messages": "Success"})
    return render(request, 'upload_excel_file.html')
