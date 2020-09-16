import os

f=open("ips.txt","r")
ips = f.readlines()
f.close()

def isup(ip):
    if os.system(f"ping {ip} > NUL") == 0:
        status = True
    else:
        status = False
    return status

for ip in ips:
    ip=ip.strip()
    if isup(ip):
        print(f"{ip} is up" )
    else:
        print("{} is down".format(ip))