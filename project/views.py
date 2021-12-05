from django.shortcuts import render
from tablib import Dataset

from .models import Person
import pandas as pd
from django.contrib import messages


def Import_csv(request):
    if request.method == 'POST':
        myfile = request.FILES['file']
        file = str(myfile)
        if not file.endswith('xlsx'):
            return render(request, 'error.html',
                          {'errors': 'the file content is not as expected'})
        else:
            df = pd.read_excel(myfile)
            for df in df.itertuples():
                obj = Person.objects.create(first_name=df.first_name, last_name=df.last_name, email=df.email)
    return render(request, 'input.html')