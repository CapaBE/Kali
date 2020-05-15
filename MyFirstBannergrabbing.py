#! /usr/bin/python3

import socket

ports = [21,22,25,3306,111,139,445,8080]

for port in ports:
    print("Trying port "+ str(port))
    try:
        s = socket.socket()
        s.connect(("192.168.1.100",port))
        answer = s.recv(1024)
        print(answer)
        s.close()
    except ConnectionRefusedError as cref:
            print("still trying...", cref)

