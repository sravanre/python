import requests

url = "http://api.open-notify.org/iss-now.json"

response = requests.get(url)

data = response.json()

print(type(data))
print(len(data))

position = data.get("iss_position")

print(type(position))
print(len(position))

latitude =  position.get('latitude')
longitude = position.get('longitude')

print(f"ISS is currently at {latitude},{longitude}")
