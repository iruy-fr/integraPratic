import os
import datetime
from dateutil.relativedelta import relativedelta, FR


def get_pasta():
    return os.path.basename(os.path.dirname(os.path.abspath(__name__)))

def caminho_clientes():
    arquivo_local = rf"{os.path.dirname(os.path.realpath(__name__))}/clientes_{caminho_data()}.txt"
    return arquivo_local


def caminho_arquivo():
    arquivo_local = rf"{os.path.dirname(os.path.realpath(__name__))}/produtos_{caminho_data()}.txt"
    return arquivo_local


def caminho_cad():
    pratic_cad = os.path.basename(rf"{get_pasta()}")
    permitidos = {'35', '41', '48', '57', '71', '83', '101', '114'}
    if pratic_cad in permitidos:
        caminho_base = os.path.dirname(os.path.realpath(__file__))
        return os.path.join(caminho_base, f"cad{pratic_cad.zfill(3)}.txt")
    return None


def cabecalho_cad():
    pratic_cad = os.path.basename(rf"{get_pasta()}")
    if pratic_cad.isdigit():
        return pratic_cad.zfill(5)
    return None


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