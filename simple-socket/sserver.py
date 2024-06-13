#server
import socket

ip = socket.gethostname()
port = 12345
buffersize = 100

skt = socket.socket()
skt.bind((ip, port))
skt.listen()

print('the server is ready...')
while True:
    con, addr = skt.accept()
    print(f"the client address is; {addr}")

    data = con.recv(buffersize).decode(encoding='utf-8')
    print(f'the received data is\n{data}')
# skt.close()
