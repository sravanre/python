import os
f=open("ips.txt","r")
ips=f.readlines()
print(ips)
f.close()
#for ip in range(len(ips)):
#print(ip)
q=open("ip_result1.txt","a")
    
    
for ipb in ips:
    ipa = ipb.strip()      # this takes out the
    print(ipa)
    exitcode = os.system(f"ping {ipa} > NUL")
    if exitcode == 0:
        print(f" {ipa} is up")
        q.write(f" {ipa} is up\n")
    else:
        print(f"{ipa} is down")
        q.write(f"{ipa} is down\n")
q.close()
