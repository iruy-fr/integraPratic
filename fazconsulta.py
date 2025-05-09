import os
import datetime
from dateutil.relativedelta import relativedelta, FR


def get_pasta():
    print(os.path.basename(os.path.dirname(os.path.realpath(__name__))))
    return os.path.basename(os.path.dirname(os.path.realpath(__name__)))

def caminho_clientes():
    arquivo_local = rf"{os.path.dirname(os.path.realpath(__name__))}/clientes_{caminho_data()}.txt"
    return arquivo_local


def caminho_arquivo():
    arquivo_local = rf"{os.path.dirname(os.path.realpath(__name__))}/produtos_{caminho_data()}.txt"
    return arquivo_local


def caminho_cad():
    pratic_cad = os.path.basename(rf"{get_pasta()}")
    arquivo_cad = os.path.dirname(os.path.realpath(__name__))
    return os.path.join(arquivo_cad, f"cad{pratic_cad.zfill(3)}.txt")



def cabecalho_cad():
    pratic_cad = os.path.basename(rf"{get_pasta()}")
    return pratic_cad.zfill(5)



def consulta_sexta():
    if relativedelta(weekday=FR(0)):
        getfriday = datetime.date.today() + relativedelta(weekday=FR(-2))
        formated_date = getfriday.strftime('%d/%m/%Y')
        return formated_date
    else:
        getfriday = datetime.date.today() + relativedelta(weekday=FR(-2))
        formated_date = getfriday.strftime('%d/%m/%Y')
        return formated_date


def caminho_data():
    getDate = datetime.date.today()
    formated_date = getDate.strftime('%d-%m-%Y')
    return formated_date


caminho_cad()