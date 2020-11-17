from  socket import *
from time  import ctime

HOST = '127.0.0.1'
PORT = 8012
BUFFSIZE = 1024
ADDR = (HOST, PORT)


# tcp
def tcp():
    client_sockfd = socket(AF_INET, SOCK_STREAM)
    client_sockfd.connect(ADDR)
    
    while True:
        data = input(">")
        if not data:
            break
        client_sockfd.send(data.encode())
        data = client_sockfd.recv(BUFFSIZE)
        if not data:
            break
        print(data.decode('utf-8'))
    client_sockfd.close()


# udp
def udp():
    client = socket(AF_INET, SOCK_DGRAM)
    while True:
        msg = input(">").strip()
        client.sendto(msg.encode('utf-8'), ADDR)
        data, server_addr = client.recvfrom(BUFFSIZE)
        print("客户端revefrom", data, server_addr)
    client.close()


udp()