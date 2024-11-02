import datetime
import pathlib
from dateutil.relativedelta import relativedelta, FR

def caminho_arquivo():
    arquivo_local = r"C:\consultatesteintegraPratic"
    return arquivo_local
def consulta_sexta():
    getfriday = datetime.date.today() + relativedelta(weekday=FR(-1))
    formated_date = getfriday.strftime('%d/%m/%Y')
    return formated_date