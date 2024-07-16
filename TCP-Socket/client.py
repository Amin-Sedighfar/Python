#CLIENT
import socket
import os
buff = 1

skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
skt.connect((socket.gethostname(),12345))

complete_rmsg = ''
while True:
    rmsg = skt.recv(buff).decode()
    if rmsg == '=':
        break
    complete_rmsg +=rmsg
print(complete_rmsg)

filesize = os.path.getsize('screenshot.png')
skt.send(str(filesize).encode())
print("\nSending the file...!!!")

file = open('screenshot.png','rb')

while True:
    data = file.read(4096)
    if not data:
        break
    skt.sendall(data)

file.close()
skt.close()
