import datetime
import os
from dateutil.relativedelta import relativedelta, FR


def get_pasta():
    return os.path.basename(r"C:\consultatesteintegraPratic/35")

def caminho_clientes():
    arquivo_local = rf"C:\consultatesteintegraPratic/consultaclientesteste{caminho_data()}.txt"
    return arquivo_local


def caminho_arquivo():
    arquivo_local = rf"C:\consultatesteintegraPratic/consultateste{caminho_data()}.txt"
    return arquivo_local


def caminho_cad():
    pratic_cad = os.path.basename(rf"{get_pasta()}")
    match pratic_cad:
        case '35':
            arquivo_local = rf"C:\consultatesteintegraPratic/{pratic_cad}/cad_35.txt"
            return arquivo_local
        case '41':
            arquivo_local = rf"C:\consultatesteintegraPratic/{pratic_cad}/cad_41.txt"
            return arquivo_local
        case '48':
            arquivo_local = rf"C:\consultatesteintegraPratic/{pratic_cad}/cad_48.txt"
            return arquivo_local
        case '57':
            arquivo_local = rf"C:\consultatesteintegraPratic/{pratic_cad}/cad_57.txt"
            return arquivo_local
        case '71':
            arquivo_local = rf"C:\consultatesteintegraPratic/{pratic_cad}/cad_71.txt"
            return arquivo_local
        case '83':
            arquivo_local = rf"C:\consultatesteintegraPratic/{pratic_cad}/cad_83.txt"
            return arquivo_local
        case '101':
            arquivo_local = rf"C:\consultatesteintegraPratic/{pratic_cad}/cad_101.txt"
            return arquivo_local
        case '114':
            arquivo_local = rf"C:\consultatesteintegraPratic/{pratic_cad}/cad_114.txt"
            return arquivo_local


def cabecalho_cad():
    pratic_cad = os.path.basename(rf"{get_pasta()}")
    match pratic_cad:
        case '35':
            cabecalho = '00035'
            return cabecalho
        case '41':
            cabecalho = '00041'
            return cabecalho
        case '48':
            cabecalho = '00048'
            return cabecalho
        case '57':
            cabecalho = '00057'
            return cabecalho
        case '71':
            cabecalho = '00071'
            return cabecalho
        case '83':
            cabecalho = '00083'
            return cabecalho
        case '101':
            cabecalho = '00101'
            return cabecalho
        case '114':
            cabecalho = '00114'
            return cabecalho


def consulta_sexta():
    getfriday = datetime.date.today() + relativedelta(weekday=FR(-1))
    formated_date = getfriday.strftime('%d/%m/%Y')
    return formated_date


def caminho_data():
    getfriday = datetime.date.today() + relativedelta(weekday=FR(-1))
    formated_date = getfriday.strftime('%d-%m-%Y')
    return formated_date