import os
ips = ["www.google.com",
       "www.intel.com",
       "www.ibm.com",
       "localhost",
       "127.0.0.1",
       "www.wellsfargopythonramesh.com"
       ]

for ip in ips:
    exitcode = os.system(f"ping {ip} > NUL")
    if exitcode == 0:
        print(f"{ip} is up" )
    else:
        print("{} is down".format(ip) )
