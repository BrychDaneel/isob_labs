from socket import socket, AF_INET, SOCK_STREAM
from time import sleep

host = 'localhost'
port = 27015
addr = (host,port)

i = 0
while True:
    i = i + 1
    tcp_socket = socket(AF_INET, SOCK_STREAM)
    tcp_socket.connect(addr)
    print('Send: ' + "Some confidential info #{}".format(i))
    tcp_socket.send("Some confidential info #{}".format(i).encode())
    data = tcp_socket.recv(1024)
    print('Recv: ' + data.decode())
    tcp_socket.close()
    sleep(5)
