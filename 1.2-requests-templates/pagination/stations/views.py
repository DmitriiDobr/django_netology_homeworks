import pandas as pd
import csv
from pagination import settings
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    #length = pd.read_csv(settings.BUS_STATION_CSV, encoding="utf-8")
    reader = csv.DictReader(open(settings.BUS_STATION_CSV))
    rows = list(reader)
    page_number = int(request.GET.get("page",1))
    paginator = Paginator(rows, per_page=200)
    page = paginator.get_page(page_number)
    print(paginator.object_list)
    context = {
         'bus_stations': paginator.object_list,
         'page': page,
    }
    return render(request, 'stations/index.html', context)
