import socket
import sys


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
            print("Connection Initialized")
        elif response[:7] == "SIGNIN:":
            print("User login:  {}".format(response.rstrip()[7:]))
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
            print("Message from: {}".format(message[0]))
            print("Content: {}".format(message[1]))
        elif response[:8] == "SIGNOFF:":
            print("User sign off: {}".format(response[8:]))
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
        if data == "1\n":
            data = "LIST\n".encode("utf-8")
        elif data == "2\n":
            to = input("Message recipient: ")
            msg = input("Message content: ")
            print("----Message sent----")
            data = "To:{}:{}".format(to, msg)
            data = (data + "\n").encode("utf-8")
        elif data == "3\n":
            print("Logging off...")
            self.Close_Connection()
        else:
            data = data.encode("utf-8")
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

