from django.shortcuts import render
from legacy.tasks import task_read
from legacy.models import Sale
import pandas as pd
import pandas.io.sql as sql
# Create your views here.
from django.http import HttpResponse
from django.views import View

class HomeView(View):
    def get(self, request):
        return render(request, "templates/home.html")


def teste(request):
    Sale.objects.all().delete()
    # result = task_read.delay()
    result = task_read()
    return render(request, "templates/home.html")

