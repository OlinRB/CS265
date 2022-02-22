import socket
import sys

class Client:
    def __init__(self, HOST, PORT):
        self.authenticated = False
        self.initialized = False
        self.HOST = HOST
        self.PORT = PORT
        self.Init_Connection()
        self.received = []

    def Init_Connection(self):
        pass
        self.s = socket.socket()
        self.s.connect((self.HOST, self.PORT))

    def Send_Data(self, message):
        self.s.sendall(bytes(message + "\n", "utf-8"))
        received = str(self.s.recv(1024), "utf-8").strip()
        if self.received == "HELLO":
            self.initialized = True

        if self.received == "AUTHYES":
            self.authenticated = True
            received = str(self.s.recv(1024), "utf-8").strip()

    def Receive(self):
        self.received = str(self.s.recv(1024), "utf-8").strip()

    def __del__(self):
        self.s.close()

