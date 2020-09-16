import glob
import time

print(glob.glob("*.*"))
print(glob.glob("*.txt"))
print(glob.glob("*.csv"))
print(glob.glob("s*.*"))

import os

for myfile in glob.glob("s*.*"):
    print(myfile, os.path.getsize(myfile))
print("*" * 50)
for myfile in glob.glob("*.txt"):
    print(myfile, os.path.getctime(myfile))
print("*" * 50)    
for myfile in glob.glob("*.txt"):
    print(myfile, time.ctime(os.path.getctime(myfile)))
print("*" * 50)    
for myfile in glob.glob("*.txt"):
    print(myfile, time.time() - os.path.getctime(myfile))
    
    
# list files created in last 3 days

age = 0.5 * 24 * 60 * 60

for myfile in glob.glob("*.*"):
    fileage = time.time() - os.path.getctime(myfile)
    if fileage  < age:
        print(myfile, fileage)
