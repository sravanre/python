import csv
from openpyxl import  Workbook

wb = Workbook()
ws = wb.active
#ws = wb['Sheet1']
f = open("marks.csv","r")

for lines in csv.reader(f):
    ws.append(lines)

f.close()
wb.save('marks1.xlsx')
wb.close()

##r=1
##for lines in csv.reader(f):
##    for c,val in enumerate(lines):
##        ws.cell(row=r,column=c+1, value=val)
##    r+=1

