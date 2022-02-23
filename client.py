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

    def Authenticate(self):
        print("Please enter your credentials")
        while not self.authenticated:
            u_name = input("Username: ")
            pwd = input("Password: ")
            credentials = "AUTH:{}:{}\n".format(u_name, pwd).encode("utf-8")
            #print("|" + credentials + "|")
            self.s.send(credentials)
            self.Read_Data()

    def Read_Data(self):
        data = str(self.s.recv(1024), "utf-8")
        if data.strip() == "AUTHYES":
            self.authenticated = True
            print("Login Successful")
        print(data)

    def Send_Data(self):
        data = sys.stdin.readline().encode("utf-8")
        self.s.send(data)


    def __del__(self):
        self.s.close()

