from  socket import *
from time  import ctime

HOST = '127.0.0.1'
PORT = 8012
BUFFSIZE = 1024
ADDR = (HOST, PORT)

# tcp
def tcp():
    sockfd = socket(AF_INET, SOCK_STREAM)
    sockfd.bind(ADDR)
    sockfd.listen(5)
    while True:
        print("waiting for connection...")
        client_sockfd, addr = sockfd.accept()
        print("... connecting from:", addr)
        while True:
            data =client_sockfd.recv(BUFFSIZE)
            print(data)
            if not data:
                break
            client_sockfd.send(('[%s] %s' %(ctime(), data)).encode())
        client_sockfd.close()
    sockfd.close()


# udp
def udp():
    udp_sockfd = socket(AF_INET, SOCK_DGRAM)
    udp_sockfd.bind(ADDR)
    while True:
        data, client_addr = udp_sockfd.recvfrom(BUFFSIZE)
        print('server 收到的数据', data)
        udp_sockfd.sendto(data.upper(), client_addr)
    udp_sockfd.close()

# tcp()
udp()