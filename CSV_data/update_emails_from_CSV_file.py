from django.shortcuts import get_object_or_404, render
import pandas as pd
from django.utils.timezone import now
from project.store_data import save_obj
from project.models import Person
from project.row import check_row
import logging


def update_email_excel_file(request):
    if request.method == 'POST':
        myfile = request.FILES['file']
        file = str(myfile)

        if not file.endswith('xlsx') or file.endswith('xls'):
            return render(request, 'messages.html',
                          {'messages': 'The File Content Is Not As Expected'})
        else:
            df = pd.read_csv(myfile)
            update_row = 0
            Invalid_row = 0
            for index, row in df.iterrows():
                if check_row(row, index):
                    Invalid_row += 1
                else:
                    try:
                        check_index = Person.objects.get(first_name=row.first_name, last_name=row.last_name)
                    except Person.DoesNotExist:
                        check_index = None
                    if check_index:
                        check_index.email = row.email
                        check_index.created_at = now
                        check_index.save()
                        update_row += 1
                    else:
                        if check_index.email == row.email:
                            return render(request, 'messages.html', {"message": "the file has the same emails, Please "
                                                                                "check your emails "})
                        save_obj(row)
            logging.debug(('Updates Row : {}'.format(update_row), 'Invalid Row: {}'.format(Invalid_row)))
            return render(request, 'messages.html', {"messages": " Updated Success"})
    return render(request, 'update_email.html')
