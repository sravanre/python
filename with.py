f=open("sample.txt","r")
for line in f:
	print(line.rstrip())
f.close()



with open("sample.txt","r") as f:
    for line in f:
        print(line.rstrip())
    print(f.closed)
print(f.closed)
