#SERVER
import socket
buff = 4096
skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
skt.bind((socket.gethostname(),12345))
skt.listen(3)

print("""\nHello there...
I'm actively listening...""")

while True:
    con, addr = skt.accept()
    print(f"the client address is {addr}")
    con.send("I got you!=".encode("UTF-8"))
    filesize = int(con.recv(buff).decode())
    print(f"the receiving file size is equal to {filesize}")
    
    recv_data = b''
    while len(recv_data) != filesize:
        data = con.recv(buff)
        if not data:
            break
        recv_data += data
        
    file = open('received_image.png',mode='wb')
    file.write(recv_data)
    file.flush()
    file.close()
