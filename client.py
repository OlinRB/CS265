import socket
import sys

class Client:
    def __init__(self, HOST, PORT):
        self.authenticated = False
        self.initialized = False
        self.HOST = HOST
        self.PORT = PORT
        self.s = socket.socket()
        self.s.connect((self.HOST, self.PORT))

    def fileno(self):
        return self.s.fileno()

    def Init_Connection(self):
        data = "HELLO\n".encode("utf-8")
        self.s.send(data)

    def Read_Data(self):
        data = str(self.s.recv(1024), "utf-8")
        print(data)

    def Send_Data(self):
        data = sys.stdin.readline().encode("utf-8")
        self.s.send(data)


    def __del__(self):
        self.s.close()

