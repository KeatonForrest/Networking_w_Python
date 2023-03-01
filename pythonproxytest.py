import requests

proxies = {
    'http': 'http://103.145.113.78:80' #find a better proxy
}

response = requests.get('https://ipinfo.io/json', proxies=proxies)
#print(response.json()['org'])
#print(response.json()['region'])
#print(response.json()['country'])
print(response.text)
