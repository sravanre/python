

import re

f=open("sample.txt","r")
q=open("sample_out.txt","a")
for se in f:
    if re.search(r"one",se):
        q.write(se)

f.close()
q.close()



`
