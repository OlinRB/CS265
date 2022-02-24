import socket
import sys

class Client:
    def __init__(self, HOST, PORT):
        self.authenticated = False
        self.initialized = False
        self.run = True
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
        response = response.rstrip()
        if response == "HELLO" and not self.initialized:
            self.initialized = True
            print("Connection Initialized")
        elif response[:7] == "SIGNIN:":
            print("User sign in:  {}".format(response.rstrip()[7:]))
        elif response == "AUTHYES":
            self.authenticated = True
            print("Login Successful")
        elif response == "AUTHNO":
            print("Invalid Credentials")
        elif response == "UNIQNO":
            print("Error: Server can only accept single connection from client")
        elif response[:5] == "From:":
            message = response[5:]
            message = message.split(":")
            print("From: {}".format(message[0]))
            print("Message: {}".format(message[1]))
        elif response[:8] == "SIGNOFF:":
            print("User sign off: {}".format(response[8:]))
        else:
            print(response)

    def Send_Data(self, input_data):

        data = sys.stdin.readline()
        # print(type(data))
        # print("|" + data + "|")
        if data == "1\n":
            print("Users online:")
            data = "LIST\n".encode("utf-8")
        elif data == "2\n":
            to = input("Message recipient: ")
            msg = input("Message content: ")
            data = "To:{}:{}".format(to, msg)
            data = (data + "\n").encode("utf-8")
        elif data == "3\n":
            self.Close_Connection()
        else:
            data = data.encode("utf-8")
        # if self.initialized and self.authenticated:
        #     exit()
        self.s.send(data)

    def Close_Connection(self):
        data = "BYE\n".encode("utf-8")
        self.s.send(data)
        self.Read_Data()
        exit()

    def __del__(self):
        self.s.close()

