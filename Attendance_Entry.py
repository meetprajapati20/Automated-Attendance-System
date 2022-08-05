from copy import copy
from xlwt import Workbook
from xlutils.copy import copy
from xlrd import open_workbook
import datetime
def present(rollno,status):
    current_time = datetime.datetime.now()

    # Workbook is created
    rb = open_workbook("Attendance_Entry.xls")
    wb = copy(rb)
    w_sheet = wb.get_sheet(0)
    if status == rollno:
        w_sheet.write(rollno, current_time.day, 'P')
    else:
        w_sheet.write(rollno, current_time.day, 'A')

    wb.save('Attendance_Entry.xls')