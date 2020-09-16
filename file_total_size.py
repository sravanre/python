

import os
import sys

'''

for i in dir(os.path):
    if "__" not in i and "_" not in i:
        print(i, end=" ")
'''
size = 0
count = 0

input = os.getcwd()
#print(input)
for dir,subdir,files in os.walk(input):    # count of files are stored in files
    for lineno,myfiles in enumerate(files):
        filename = os.path.join(dir,myfiles)
        filesize = os.path.getsize(filename)
        print(lineno,filename,filesize)
        size = size + filesize
        count = count + 1
print()
print(f"{size} = total size in bytes")
print("Number of file in folder {} is {}".format(os.getcwd(),count))



if size > 100000000:
    size = size/(1024*1024*1024)
    measure = "GB"
elif size > 1000000:
    size = size/(1024*1024)
    measure = "MB"
elif size > 1000:
    size = size/1024
    measure = "KB"

print(f"{size} {measure}")
        
        





'''print(files)
    print()
    print(type(files))
    print('0' * 50)
    print(dir)
    print(type(dir))'''


