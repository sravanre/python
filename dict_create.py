



# Readthe config file and create a dictionary from the data

# read the 'config.txt'

f = open("config.txt", "r")

config_data={}

for line in f:
    parts=line.split('=')
    config_data[parts[0].strip()] = parts[1].strip()

searchkey=input("enter parameter: ")
print(config_data[searchkey])
