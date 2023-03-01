import requests

payload = {'page': 2, 'count': 25}
r = requests.get('https://knurling.io')

#print(r.ok)
print(r.status_code)
#print(r.json())