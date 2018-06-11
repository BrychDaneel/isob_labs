from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread


def proc(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(data.decode())
        conn.send(data)
    conn.close()


host = 'localhost'
port = 27015
addr = (host,port)

tcp_socket = socket(AF_INET, SOCK_STREAM)
tcp_socket.bind(addr)

tcp_socket.listen(100)


while True:
    conn, addr = tcp_socket.accept()
    th = Thread(target=proc, args=(conn,))
    th.start()

tcp_socket.close()
