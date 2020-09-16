import datetime

d = datetime.datetime.now()
print(d)
print(d.year)
print(d.month)
print(d.day)
print(d.hour)

print(d.strftime("%d/%m/%y"))

for x in dir(d):
    if not x.startswith("__"):
        print(x)
        
today = datetime.datetime.today()
someday = datetime.datetime(1947,8,15)

print((today - someday).days)
