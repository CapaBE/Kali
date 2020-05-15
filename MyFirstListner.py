#! /usr/bin/python3

import socket

s = socket.socket()
s.bind(("192.168.1.100",6996))
s.listen(1)
conn, addr = s.accept()
print("Connection address: ", addr)

while True:
    data = conn.recv(100)
    if not data:
        break
    print("Received data: ", data)
    conn.send(data) #echo
conn.close()