import socket
from threading import Thread


server='192.168.0.28'
port = 2020

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server, port))
run=True
def task1():
    global run
    while run:
        try:
            in_data = client.recv(4096)
            print(in_data.decode())
        except:
            print("Соединение разорвано")


def task2():
    global run
    while run:
        out_data= input()
        client.sendall(bytes(out_data, 'UTF-8'))
        print(f'Отправлено: {str(out_data)}')
        if out_data=='exit':
            run=False
            client.close()
            exit()
            


t1=Thread(target=task2)
t2=Thread(target=task1)

t1.start()
t2.start()

# t1.join()
# t2.join()



