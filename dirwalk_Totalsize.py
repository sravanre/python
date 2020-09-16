import os

# A function to convert size in bytes to KBs, MBs and GBs
def convert_size(size):
        measure="bytes"
        if(size>1000000000):
                size=size/(1024*1024*1024)
                measure="GB"
        elif(size>1000000):
                size=size/(1024*1024)
                measure = "MB"
        elif(size>1000):
                size=size/1024
                measure = "KB"
        return [size,measure]           # return both size and measure
        
size=0
count=0
for (dirname, subdir, files) in os.walk(os.getcwd()):
        for myfile in files:
                filename=os.path.join(dirname,myfile)
                if filename.endswith('.txt'):
                        size=size+os.path.getsize(filename)
                        count=count+1
                        
s = convert_size(size)  
avg = convert_size(size/count)

print(f" Total files: {count}")
print(f"Total size {s[0]}{s[1]}")
print(f"Average size: {avg}")
