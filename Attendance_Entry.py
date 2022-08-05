import xlwt
from xlwt import Workbook
import datetime
def present(rollno):
    # Writing to an excel
    # sheet using Python
    current_time = datetime.datetime.now()

    # Workbook is created
    wb = Workbook()

    # add_sheet is used to create sheet.
    sheet1 = wb.add_sheet('Sheet 1')
    sheet1.write(rollno, current_time.day, 'P')


    wb.save('xlwt_example.xls')
