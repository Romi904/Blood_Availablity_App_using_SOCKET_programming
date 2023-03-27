#Code By Romijul Laskar
# Dt Mon Feb 13 10:35
import socket
import threading
s=socket.socket()
s.bind(('127.0.0.1',5029))
s.listen(3)
print('Waiting for connection....')
print('Waiting For DNS To Respond....')

A = 47
B = 20
AB = 2
connect = True
while connect:
    cli,address = s.accept()
    data=cli.recv(1024).decode()
    if data == 'A':
        print('Received Request Available Blood :',A,'Bottles of group ',data)
        x='Available '+str(A)
        cli.send(x.encode('ascii'))
        break
    elif data == 'B':
        print('Received Request Available Blood :',B,'Bottles of group ',data)
        x='Available '+A
        cli.send(x.encode('ascii'))
        break
    elif data == 'AB':
        print('Received Request Available Blood :',AB,'Bottles of group ',data)
        x='Available '+A
        cli.send(x.encode('ascii'))
        break