import socket
import sys

class Client:
    def __init__(self, HOST, PORT):
        self.state = "pending"
        self.HOST = HOST
        self.PORT = PORT
        self.Init_Connection()

    def Init_Connection(self):
        pass
        self.s = socket.socket()
        self.s.connect((self.HOST, self.PORT))

    def Send_Data(self, message):
        self.s.sendall(bytes(message + "\n", "utf-8"))
        self.received = str(self.s.recv(1024), "utf-8")

    def Close_Connection(self):
        self.s.close()

