import socket, threading
from arpscan import scan

localhost='192.168.0.28'
port = 2020

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((localhost, port))
print("Сервер запущен!")

class CLientThread(threading.Thread):

    def __init__(self, clientaddr, clientsocket):
        threading.Thread.__init__(self)
        self.clientaddr= clientaddr
        self.csocket=clientsocket
        print("Новое подключение: ", self.clientaddr)
    def run(self):
        msg=''
        while True:
            data=self.csocket.recv(4096)
            msg=data.decode()
            print(f'От клиента({self.clientaddr}): {msg}')
            if msg == '':
                print('Отключение')
                break 
            if 'arpscan' in msg:
                target_ip=str(msg.split('-')[1])
                clients_list=scan(target_ip)
                clientsock.send(bytes('IP\t\t\t\tMAC Adress\n-----------------------------------------------', "UTF-8"))
                # print(clients_list)
                for el in clients_list:
                    clientsock.send(bytes(el.get("IP") + '\t\t' + el.get("MAC")+"\n", "UTF-8"))
                    clientsock.send(bytes('-----------------------------------------------\n', "UTF-8"))    
            if msg == 'exit':
                print('Отключение')
                break
      
            
while True:
    server.listen(1)
    clientsock, clientaddr = server.accept()
    newthread = CLientThread(clientaddr, clientsock)
    newthread.start()


    
