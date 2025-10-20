from datetime import date, datetime, timedelta

def data_atual():
    return date.today()

def formatar_data(data):
    return data.strftime("%d/%m/%Y")

def dias_ate(data_futura):
    hoje = date.today()
    delta = data_futura - hoje
    return delta.days
