from django.shortcuts import render
from .models import Person
import pandas as pd
import logging

logging.basicConfig(filename='person_log.log', level=logging.DEBUG)


def Import_csv(request):
    if request.method == 'POST':
        myfile = request.FILES['file']
        file = str(myfile)
        if not file.endswith('xlsx'):
            return render(request, 'error.html',
                          {'errors': 'the file content is not as expected'})
        else:
            df = pd.read_excel(myfile)
            for index, row in df.iterrows():
                if pd.isna(row[0]):
                    logging.debug(row)
                    continue
                else:
                    obj = Person.objects.create(first_name=row.first_name, last_name=row.last_name, email=row.email)
    return render(request, 'input.html')

