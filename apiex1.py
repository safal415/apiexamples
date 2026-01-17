import requests

myurl = "https://api.chucknorris.io/jokes/random"
response = requests.get(myurl)
data = response.json()
print(data['value'])