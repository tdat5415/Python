import socket

s = socket.socket()         

s.bind(('0.0.0.0', 8090 ))
s.listen(0)                 

while True:

    client, addr = s.accept()

    while True:
        content = client.recv(32)
        if len(content) ==0:
           break
        else:
            print(addr[0] + ' : ' + content.decode())

    client.close()
