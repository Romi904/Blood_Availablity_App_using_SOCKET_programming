#Code By Romijul Laskar
# Dt Mon Feb 13 10:35
import socket
import threading
s=socket.socket()
s.bind(('127.0.0.0',9999))
s.listen(3)
print('Waiting for connection....')


print('Waiting For Client To Respond....')
def newClientHandler(cli,ip):
    connect = True
    while connect:
        data = cli.recv(1024).decode()
        data=data.split(",",2)
        opr = data[0]
        
        print('Received : ',data)

        if opr == 'A' :
            c=socket.socket()
            c.connect(('127.0.0.1',5021))
            while True :
                if data[1]=='kolkata':
                    x=data[0]
                    c.send(x.encode('ascii'))
                    output1=c.recv(1024).decode()
                    cli.send(output1.encode('ascii'))
                elif data[1]=='durgapur' :
                    c=socket.socket()
                    c.connect(('127.0.0.1',5024))
                    x=data[0]
                    c.send(x.encode('ascii'))
                    output1=c.recv(1024).decode()
                    cli.send(output1.encode('ascii'))
                elif data[1]=='asansol' :
                    c=socket.socket()
                    c.connect(('127.0.0.1',5025))
                    x=data[0]
                    c.send(x.encode('ascii'))
                    output1=c.recv(1024).decode()
                    cli.send(output1.encode('ascii'))
                break

        elif opr == 'B':
            a=socket.socket()
            a.connect(('127.0.0.1',5022))
            while True :
                if data[1]=='kolkata':
                    x=data[0]
                    c.send(x.encode('ascii'))
                    output1=c.recv(1024).decode()
                    cli.send(output1.encode('ascii'))
                elif data[1]=='durgapur' :
                    c=socket.socket()
                    c.connect(('127.0.0.1',5026))
                    x=data[0]
                    c.send(x.encode('ascii'))
                    output1=c.recv(1024).decode()
                    cli.send(output1.encode('ascii'))
                elif data[1]=='asansol' :
                    c=socket.socket()
                    c.connect(('127.0.0.1',5027))
                    x=data[0]
                    c.send(x.encode('ascii'))
                    output1=c.recv(1024).decode()
                    cli.send(output1.encode('ascii'))
                break
        elif opr == 'AB':
            b=socket.socket()
            b.connect(('127.0.0.1',5023))
            while True :
                if data[1]=='kolkata':
                    x=data[0]
                    c.send(x.encode('ascii'))
                    output1=c.recv(1024).decode()
                    cli.send(output1.encode('ascii'))
                elif data[1]=='durgapur' :
                    c=socket.socket()
                    c.connect(('127.0.0.1',5028))
                    x=data[0]
                    c.send(x.encode('ascii'))
                    output1=c.recv(1024).decode()
                    cli.send(output1.encode('ascii'))
                elif data[1]=='asansol' :
                    c=socket.socket()
                    c.connect(('127.0.0.1',5029))
                    x=data[0]
                    c.send(x.encode('ascii'))
                    output1=c.recv(1024).decode()
                    cli.send(output1.encode('ascii'))
                break
        else :
            cli.send("No data")

while True:
    cli,ip=s.accept()
    threading._start_new_thread(newClientHandler(cli,ip))