
import os
def isup(ip):
    if os.system(f"ping {ip} > NUL") == 0:
        status = True
    else:
        status = False
    return status
