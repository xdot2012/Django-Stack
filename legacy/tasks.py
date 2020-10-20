from celery import shared_task
import pandas as pd
from legacy.models import Sale
from celery.schedules import crontab

@shared_task
def task_read():
    df = pd.read_csv('videogamesales/vgsales.csv', sep=',',  encoding='iso8859-15')
    vendas_antigas = Sale.objects.all()
    vendas_antigas.delete()

    df['Name'] = df['Name'].astype('string')
    df['Platform'] = df['Platform'].astype('string')
    df['Genre'] = df['Genre'].astype('string')
    df['Publisher'] = df['Publisher'].astype('string')
    df['Year'] = df['Year'].fillna(0).astype('int32')

    df = df.drop(columns=['Global_Sales'])
    df.columns = map(str.lower, df.columns)  # TO LOWER

    lista = []
    for x in df.T.to_dict().values():
        lista.append(Sale(**x))

    Sale.objects.bulk_create(lista)
    df = df.to_json()

    return df
