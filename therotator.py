import requests
import queue
import threading

q = queue.Queue()
valid_proxies = []

with open("") as f: # <- Make new proxylist with .txt file
    proxies = f.read().split("\n")
    for p in proxies:
        q.put(p)
            
def check_proxies():
    global q
    while not q.empty():
        proxy = q.get()
        try:
            res = requests.get("https://ipinfo.io/json", 
                               proxies={"http": proxy,
                                        "https": proxy})
        except:
            continue
        if res.status_code == 200:
            print(proxy)
            
for _ in range(10):
     threading.Thread(target=check_proxies).start()