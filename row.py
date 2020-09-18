
from openpyxl import Workbook


wb = Workbook()
ws=wb.active

for rowno in range(1,101):
    ws.cell(row=rowno,column=1,value=rowno)

wb.save("row.csv")

