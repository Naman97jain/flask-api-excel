import xlrd
import app_config as config
from collections import OrderedDict
import datetime
import pytz

def read_from_workbook(data):
    data_list = []
    wb = xlrd.open_workbook(file_contents=data)
    sh = wb.sheet_by_index(0)
    for rownum in range(1, sh.nrows):
        data = OrderedDict()
        row_values = sh.row_values(rownum)
        data['Engine Number'] = str(int(row_values[0]))
        data['Chassis Number'] = str(int(row_values[1]))
        data_list.append(data)

    return data_list

def get_current_date():
    tz = pytz.timezone(config.LOCAL_TIME)
    date = datetime.datetime.now(tz).date()
    return str(date)