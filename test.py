import socket
import sys
import select

def connect():
    connection = socket.socket()
    HOST, PORT = "132.198.11.12", 12000
    connection.connect((HOST, PORT))
    return connection
while True:
    connection = connect()
    readers,_,_= select.select([sys.stdin,connection],[],[])
    for reader in readers:
        if reader is connection:
            print(connection.recv(1000).decode("utf8"))
        else:
            msg = sys.stdin.readline()
            connection.send(msg.encode("utf8"))