import datetime
from dateutil.relativedelta import relativedelta, FR


def caminho_clientes():
    arquivo_local = rf"C:\consultatesteintegraPratic/consultaclientesteste{caminho_data()}.txt"
    return arquivo_local

def caminho_arquivo():
    arquivo_local = rf"C:\consultatesteintegraPratic/consultateste{caminho_data()}.txt"
    return arquivo_local

def caminho_cad():
    arquivo_local = rf"C:\consultatesteintegraPratic/cad_{caminho_data()}.txt"
    return arquivo_local
def consulta_sexta():
    getfriday = datetime.date.today() + relativedelta(weekday=FR(-1))
    formated_date = getfriday.strftime('%d/%m/%Y')
    return formated_date


def caminho_data():
    getfriday = datetime.date.today() + relativedelta(weekday=FR(-1))
    formated_date = getfriday.strftime('%d-%m-%Y')
    return formated_date