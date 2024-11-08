import os
import datetime
from dateutil.relativedelta import relativedelta, FR


def get_pasta():
    #ATIVAR ANTES DE ENVIAR PARA O PRATIC
    return os.path.basename(os.path.dirname(os.path.abspath(__name__)))
    #return os.path.basename(r"\\192.168.99.10/c$/35")

def caminho_clientes():
    arquivo_local = rf"{os.path.dirname(os.path.realpath(__name__))}/clientes_{caminho_data()}.txt"
    #arquivo_local = rf"C:\consultatesteintegraPratic/consultaclientesteste{caminho_data()}.txt"
    return arquivo_local


def caminho_arquivo():
    arquivo_local = rf"{os.path.dirname(os.path.realpath(__name__))}/produtos_{caminho_data()}.txt"
    #arquivo_local = rf"C:\consultatesteintegraPratic/consultateste{caminho_data()}.txt"
    return arquivo_local


def caminho_cad():
    pratic_cad = os.path.basename(rf"{get_pasta()}")
    match pratic_cad:
        case '35':
            arquivo_local = rf"{os.path.dirname(os.path.realpath(__name__))}/cad035.txt"
            #arquivo_local = rf"C:\consultatesteintegraPratic/{pratic_cad}/cad035.txt"
            return arquivo_local
        case '41':
            arquivo_local = rf"{os.path.dirname(os.path.realpath(__name__))}/cad041.txt"
            # arquivo_local = rf"C:\consultatesteintegraPratic/{pratic_cad}/cad035.txt"
            return arquivo_local
        case '48':
            arquivo_local = rf"{os.path.dirname(os.path.realpath(__name__))}/cad048.txt"
            # arquivo_local = rf"C:\consultatesteintegraPratic/{pratic_cad}/cad035.txt"
            return arquivo_local
        case '57':
            arquivo_local = rf"{os.path.dirname(os.path.realpath(__name__))}/cad057.txt"
            # arquivo_local = rf"C:\consultatesteintegraPratic/{pratic_cad}/cad035.txt"
            return arquivo_local
        case '71':
            arquivo_local = rf"{os.path.dirname(os.path.realpath(__name__))}/cad071.txt"
            # arquivo_local = rf"C:\consultatesteintegraPratic/{pratic_cad}/cad035.txt"
            return arquivo_local
        case '83':
            arquivo_local = rf"{os.path.dirname(os.path.realpath(__name__))}/cad083.txt"
            # arquivo_local = rf"C:\consultatesteintegraPratic/{pratic_cad}/cad035.txt"
            return arquivo_local
        case '101':
            arquivo_local = rf"{os.path.dirname(os.path.realpath(__name__))}/cad101.txt"
            # arquivo_local = rf"C:\consultatesteintegraPratic/{pratic_cad}/cad035.txt"
            return arquivo_local
        case '114':
            arquivo_local = rf"{os.path.dirname(os.path.realpath(__name__))}/cad114.txt"
            # arquivo_local = rf"C:\consultatesteintegraPratic/{pratic_cad}/cad035.txt"
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
    if relativedelta(weekday=FR(0)):
        getfriday = datetime.date.today() + relativedelta(weekday=FR(-2))
        formated_date = getfriday.strftime('%d/%m/%Y')
        return formated_date
    else:
        getfriday = datetime.date.today() + relativedelta(weekday=FR(-2))
        formated_date = getfriday.strftime('%d/%m/%Y')
        return formated_date


def caminho_data():
    getfriday = datetime.date.today() + relativedelta(weekday=FR(-1))
    formated_date = getfriday.strftime('%d-%m-%Y')
    return formated_date