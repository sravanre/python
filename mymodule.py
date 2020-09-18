

import os
def isup(ip):
    if os.system(f"ping {ip} > NUL") == 0:
        status = True
    else:
        status = False
    return status



import subprocess

def isup1(ip):
    exitcode=subprocess.call(["ping","-n","1",ip],stdout=subprocess.PIPE)
    if exitcode == 0:
        status = True
    else:
        status = False
    return status

def isup2(ip):
    return not subprocess.call(["ping","-n","1",ip],stdout=subprocess.PIPE)
    
