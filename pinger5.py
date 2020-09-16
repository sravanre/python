
import os
from mymodule import isup

f=open("ips.txt","r")
ips = f.readlines()
f.close()


for ip in ips:
    ip=ip.strip()
    if isup(ip):
        print(f"{ip} is up" )
    else:
        print("{} is down".format(ip))
