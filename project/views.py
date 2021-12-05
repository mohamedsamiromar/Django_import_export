from django.shortcuts import render
from .models import Person
import pandas as pd


def Import_csv(request):

    if request.method == 'POST':
        myfile = request.FILES['file']
        df = pd.read_excel(myfile)
        for df in df.itertuples():
            obj = Person.objects.create(first_name=df.first_name, last_name=df.last_name, email=df.email)
    return render(request, 'input.html')
















