'''
a = [1,2,3]
x,y,z=a
for i in [x,y,z]:
    print(i end("")
    '''


"""
unpacking and split  function usage 
line = "sravan,u744353,9108412191"
name,empid,number = line.split(",")
print(name)
print(empid)
print(number)
"""

'''
#strip()   - used to strip out the white spaces .
# usefull when getiing the logs cleaar the white spcaes 

line = "     hello how are you sravan     \n"
line
print(line)
print("--->{}<---".format(line))
print("--->{}<---".format(line.lstrip()))

print("--->{}<---".format(line.rstrip))
print("--->{}<---".format(line.rstrip()))

print("--->{}<---".format(line.strip()))

'''


'''
def sum(a,b):
    return a+b

num1 = int(input("enter number:"))
num2 = int(input("enter number2:"))

print(sum(num1,num2))

'''

'''
f=open("marks.csv","r")
#new1=f.read()
for new2 in f :
    student_name,s1,s2,s3 = new2.strip().split(",")
    print(student_name)

f.close()

'''

'''

f=open("marks.csv","r")
new1=f.readlines()
for new2 in new1:
    name,s1,s2,s3 = new2.split(",")
    print("{}marks are {}".format(name,int(s1)+int(s2)+int(s3)))
f.close()

'''







'''

import os
f=open("ips.txt","r")
ips=f.readlines()
print(ips)
f.close()
#for ip in range(len(ips)):
#print(ip)
q=open("ip_result1.txt","a")
    
    
for ipb in ips:
    ipa = ipb.strip()
    exitcode = os.system(f"ping {ipa} > NUL")
    if exitcode == 0:
        print(f" {ipa} is up")
        q.write(f" {ipa} is up\n")
    else:
        print(f"{ipa} is down")
        q.write(f"{ipa} is down\n")
q.close()


'''

'''

#time .py
import time
print(time.time())

start = time.time()
for x in range(100000):
    y=x*x
end = time.time()

print(end - start)

time.sleep(2)

print(time.ctime())
print(time.ctime(time.time()))



'''
'''

# file comparision
import filecmp/

file1 = "sample.txt"
file2 = "sample1.txt"

print(filecmp.cmp(file1,file2))

'''

import sys
import os

if len(sys.argv) == 3:
    filename = sys.argv[1]
    pattern = sys.argv[2]
else:
    print("Usage: searchfile5.py <filename> <pattern>")
    sys.exit()
    
f=open("sample.txt",'r')
for lineno,line in enumerate(f):
    #print(line,end="")
    if pattern.lower() in line.lower():
        print(lineno + 1, line.rstrip())
f.close()



























      







