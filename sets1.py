servers = {"server34","server45","server52","server89"}
dservers = {"server34","server89"}

colors1 = {"blue","red","pink","green"}
colors2 = {"red","blue","white","black"}

print(type(colors1))
print(colors1.union(colors2))
print(colors1.intersection(colors2))

print(servers - dservers)

nums = [3,4,5,6,7,8,3,4,5,6,7,23,4,5,6,7,8,9,23,4,5,6,7,6]
print(set(nums))  # removes duplicates
