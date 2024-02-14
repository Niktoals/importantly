import os
import socket
from ipaddress import *
from time import *

def ping(address):
    return not bool(os.system('ping %s -n 1' % (address,)))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
net=ip_network('192.168.0.28/255.255.255.0', 0)
for addr in net:
    sleep(0.5)
    try:
        client.connect((str(addr), 2020))
        print("Подключено", addr)
        client.shutdown()
        break
    except:
        print("Не удалось подключиться", addr)


