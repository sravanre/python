import os
ips = ["www.google.com","www.intel.com","www.ibm.com",
       "localhost","www.cartoon.net"]

for ip in ips:
    exitcode = os.system(f"ping {ip} > NUL")
    if exitcode == 0:
        print(f"{ip} is up")
    else:
        print(f"{ip} is down")
    #print(f"{ip} is up")
    
