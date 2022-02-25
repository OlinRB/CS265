import socket
import sys

"""
Client class drives functionality of chat.py 
creating a connection to the server and 
holding decision structures to read/write 
data.

"""


class Client:
    def __init__(self, HOST, PORT):
        self.authenticated = False
        self.initialized = False
        self.closed = False
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
            print("\nConnection Initialized")
        elif response[:7] == "SIGNIN:":
            print("--------------------")
            print("User login:  {}".format(response.rstrip()[7:]))
            print("--------------------")
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
            print("---------------------")
            print("Message from: {}".format(message[0]))
            print("Content: {}".format(message[1]))
            print("---------------------")
        elif response[:8] == "SIGNOFF:":
            print("--------------------")
            print("User sign off: {}".format(response[8:]))
            print("--------------------")
        elif "," in response or response.islower():
            print("-------------")
            print("Users online:")
            users = response.split(",")
            for user in users:
                print(user.replace(" ", ""))
            print("-------------")
        else:
            pass
        print("\n")

    def Send_Data(self):
        data = sys.stdin.readline()
        good_input = False
        if data == "1\n":
            good_input = True
            data = "LIST\n".encode("utf-8")
        elif data == "2\n":
            good_input = True
            to = input("Message recipient: ")
            msg = input("Message content: ")
            print("-----Message sent-----")
            data = "To:{}:{}".format(to, msg)
            data = (data + "\n").encode("utf-8")
        elif data == "3\n":
            good_input = True
            print("Logging off...")
            self.Close_Connection()
        else:
            data = data.encode("utf-8")
        if good_input:
            self.s.send(data)

    def Close_Connection(self):
        data = "BYE\n".encode("utf-8")
        self.s.send(data)
        self.Read_Data()
        self.s.close()
        self.closed = True
        exit()

    def __del__(self):
        self.s.close()

