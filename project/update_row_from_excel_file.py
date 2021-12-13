from django.shortcuts import get_object_or_404, render
import pandas as pd
from django.utils.timezone import now
from .store_data import save_obj
from .models import Person
from .row import check_row
import logging


def update_email_excel_file(request):
    if request.method == 'POST':
        myfile = request.FILES['file']
        if myfile is None:
            return render(request, 'messages.html', {"messages": "Please, Upload Your File"})
        file = str(myfile)

        if not file.endswith('xlsx') or file.endswith('xls'):
            return render(request, 'messages.html',
                          {'messages': 'The File Content Is Not As Expected'})
        else:
            df = pd.read_excel(myfile)
            update_row = 0
            Invalid_row = 0
            for index, row in df.iterrows():
                if check_row(row, index):
                    Invalid_row += 1
                else:
                    try:
                        get_row = Person.objects.get(email=row.email)
                    except Person.DoesNotExist:
                        get_row = None
                    if get_row:
                        get_row.country = row.country
                        get_row.city = row.city
                        get_row.job_title = row.job_title
                        get_row.created_at = now()
                        get_row.save()
                        update_row += 1
                    elif get_row.email == row.email:

                        return render(request, 'messages.html', {"message": "the file has the same emails, Please "
                                                                            "check your emails "})
                    else:
                        save_obj(row)
            logging.debug(('Updates Row : {}'.format(update_row), 'Invalid Row: {}'.format(Invalid_row)))
            return render(request, 'messages.html', {"messages": " Updated Success"})
    return render(request, 'update_excel.html')
