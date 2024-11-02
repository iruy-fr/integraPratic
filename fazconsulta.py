import datetime
from dateutil.relativedelta import relativedelta, FR

def consulta_sexta():
    getfriday = datetime.date.today() + relativedelta(weekday=FR(-1))
    formated_date = getfriday.strftime('%d/%m/%Y')
    return formated_date