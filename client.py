import socket
s=socket.socket()
s.connect(('127.0.0.0',9999))
print("\n****************Welcome to Blood Availablity server******************\n")

while True:
    data=input('Enter Your Blood Group A , AB , B+ :')
    location = input('Enter Your Location ')
    message = data + ',' + location
    s.send(message.encode('ascii'))
    output=s.recv(246).decode()
    print('The Blood Is available at ',location,' availablity ',output)
