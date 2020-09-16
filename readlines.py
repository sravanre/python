f=open("sample.txt","r")
lines = f.readlines()

print("Line count = ", len(lines))
print("First Line = ", lines[0])
print("Last Line = ", lines[-1])
print("Lines 2 to 4 = ", lines[1:4])

f.close()