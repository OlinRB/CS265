import socketserver

"""
UVMPM cmd line chat interface

servers listening at port: 12000

Handshake->Authentication->Request/Response
Server IP: 132.198.11.12–

"""

from client import Client
import select
import sys
import socket



def connect():
    # HOST = input("Please enter the server IPv4 address: ")
    # PORT = input("Please enter the port number: ")
    HOST, PORT = "132.198.11.12", 12000
    # client = socket.socket()
    # client.connect((HOST, PORT))
    client = Client(HOST, PORT)
    message = "HELLO"
    client.Send_Data(message)
    print(str(client.s.recv(1024), "utf-8").strip())
    # client.sendall(bytes(message + "\n", "utf-8"))
    # print(str(client.recv(1024), "utf-8").strip())
    return client

def authenticate(client):
    un = input("Please enter your username: ")
    pwd = input("Please enter your password: ")
    un_pwd = "AUTH:{}:{}".format(un,pwd)
    client.s.sendall(bytes(un_pwd + "\n", "utf-8"))
    #print(str(client.s.recv(1024), "utf-8").strip())
    if str(client.s.recv(1024), "utf-8").strip() == "AUTHYES":
        client.authenticated = True


def menu_options():
    print("Choose an option")
    print("1. List online users")
    print("2. Send someone a message")
    print("3. Sign off")

def test(client):
    data = "HELLO"
    client.Send_Data(data)
    print(client.received)

    data = "AUTH:test1:p001"
    client.Send_Data(data)
    print(client.received)

def main():


    client = connect()

    while not client.authenticated:
        authenticate(client)
    run = True
    while run:
        #menu_options()
        readers, _, _ = select.select([client.s], [], [])
        for reader in readers:
            if reader is client:
                print(client.s.recv(1000).decode("utf8"))
            else:
                i = sys.stdin.readline()
                if i == "exit":
                    run = False
                else:
                    client.Send_Data(i)






        # choice = input("Choice: ")
        # if choice == "1":
        #     client.Send_Data("LIST")
        #     print(client.received)
        # elif choice == "2":
        #     recipient = input("Message recipient: ")
        #     message = input("Enter your message: ")
        #     data = "To:{}:{}".format(recipient, message)
        #     client.Send_Data(data)
        #     print("Message sent")
        # else:
        #     print("Goodbye")
        #     run = False





main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
