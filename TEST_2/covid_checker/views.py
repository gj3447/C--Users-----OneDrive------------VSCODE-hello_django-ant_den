from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .api import check_covid


def index(request):
    date, data = check_covid()
    return render(request, 'covid_checker/main.html', 
        {'date': date, 'domestic': data[0], 'abroad': data[1],
         'confirm': data[2], 'release': data[3], 'isolation': data[4],
         'death': data[5], 'accTest': data[6], 'accTestFin': data[7],
         'accPosRate': data[8]})