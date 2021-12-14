import pandas as pd
from django.shortcuts import render
from .store_data import save_obj


def try_view(request):
    if request.method == 'POST':
        myfile = request.FILES['file']
        df = pd.read_excel(myfile)
        df.dropna(
            axis=0,
            how='any',
            thresh=None,
            subset=None,
            inplace=True
        )
        for index, row in df.iterrows():
            save_obj(row)
        return render(request, 'messages.html', {"messages": "drop empty row"})
    return render(request, 'upload_excel_file.html')
