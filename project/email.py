from django.shortcuts import get_object_or_404, render
import pandas as pd
from django.utils.timezone import now
from . store_data import save_obj
from .models import Person
from . row import check_row
import logging


def update_email(request):
    if request.method == 'POST':
        myfile = request.FILES['file']
        file = str(myfile)

        if not file.endswith('xlsx') or file.endswith('xls'):
            return render(request, 'messages.html',
                          {'messages': 'The File Content Is Not As Expected'})
        else:
            df = pd.read_excel(myfile)
            update_row = 0
            for index, row in df.iterrows():
                if check_row(row, index):
                    check_index = Person.objects.get(pk=index)
                    if check_index is True:
                        person = Person()
                        person.email = check_index.email
                        person.created_at = now
                        person.save()
                        update_row += 1
                    else:
                        save_obj(row)
            logging.debug("Update Row: {}".format(update_row))
