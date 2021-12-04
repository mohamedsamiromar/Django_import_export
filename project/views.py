from django.shortcuts import render

from .models import  Person
import pandas as pd


def Import_csv(request):

    if request.method == 'POST':

        myfile = request.FILES['file']

        empexceldata = pd.read_excel(myfile)
        dbframe = empexceldata
        for dbframe in dbframe.itertuples():
            obj = Person.objects.create(first_name=dbframe.first_name, last_name=dbframe.last_name, email=dbframe.email)
        return render(request, 'input.html')















