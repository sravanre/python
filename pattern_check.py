
import os

f = open("sample.txt","r")

for line in f:
    if 'th' in line:
        print(line, end="")

f.close()
