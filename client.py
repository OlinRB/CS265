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
        self.Init_Connection()

    def fileno(self):
        return self.s.fileno()

    def Init_Connection(self):
        data = "HELLO\n".encode("utf-8")
        self.s.send(data)
        self.Read_Data()


    def Authenticate(self):
        print("Please enter your credentials")
        u_name = input("Username: ")
        pwd = input("Password: ")
        credentials = "AUTH:{}:{}\n".format(u_name, pwd).encode("utf-8")
        self.s.send(credentials)
        self.Read_Data()

    def Read_Data(self):
        response = str(self.s.recv(1024), "utf-8")
        if response.rstrip() == "HELLO" and not self.initialized:
            self.initialized = True
            print("Connection Initialized")
        elif response.rstrip()[:7] == "SIGNIN:":
            print("User sign in:  {}".format(response.rstrip()[7:]))
        elif response.rstrip() == "AUTHYES":
            self.authenticated = True
            print("Login Successful")
        elif response.rstrip() == "AUTHNO":
            print("Invalid Credentials")
        elif response.rstrip() == "UNIQNO":
            print("Error: Server can only accept single connection from client")
        else:
            print(response)


    def Send_Data(self):
        print("Please choose an option:")
        print("1) List online users")
        print("2) Send a message")
        print("3) Sign off")
        data = sys.stdin.readline().encode("utf-8")
        self.s.send(data)


    def __del__(self):
        self.s.close()

