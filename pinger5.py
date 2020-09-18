
import os
from mymodule import isup,isup1,isup2

f=open("ips.txt","r")
ips = f.readlines()
f.close()


for ip in ips:
    ip1=ip.strip()
    if isup1(ip1):
        print(f"{ip} is up" )
    else:
        print("{} is down".format(ip1))
