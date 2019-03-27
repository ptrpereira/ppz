from urllib.request import urlopen
import json

url = 'http://api.icndb.com/jokes/'
request = urlopen(url)
response = request.read()

data = json.loads(response)
print(data)

