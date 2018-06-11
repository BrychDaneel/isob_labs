#!/usr/bin/env python3

from socket import socket, AF_INET, SOCK_STREAM

host = 'localhost'
port = 27015
addr = (host,port)

cnt = 0



while True:

    tcp_socket = socket(AF_INET, SOCK_STREAM)
    tcp_socket.connect(addr)
    #print('connected')

