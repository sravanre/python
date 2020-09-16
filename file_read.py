f=open("sample.txt","r")
print(f.read())
f.close()

f=open("sample.txt","r")
for line in f:
    print(line.rstrip())
f.close()

f=open("sample.txt","r")
for line in f:
    print(line, end = "")
f.close()

print()

f=open("sample.txt","r")
for lineno,line in enumerate(f):
    print(lineno + 1, line, end = "")
f.close()
