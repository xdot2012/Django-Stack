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
        context = {}
        if request.user.is_authenticated:

            df = Sale.get_df()
            if(not df.empty):
                df = df.to_html(index=False)
            context = {
                'df': df 
            }

        return render(request, "templates/home.html", context)


def teste(request):
    Sale.objects.all().delete()
    # result = task_read.delay()
    df = task_read()
    Sale.create_from_dataframe(df)
    return render(request, "templates/home.html", {'data': df.to_json()})

