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
    client = Client(HOST, PORT)
    client.Send_Data("HELLO")
    return client

def authenticate(client):
    un = input("Please enter your username: ")
    pwd = input("Please enter your password: ")
    un_pwd = "AUTH:{}:{}".format(un,pwd)
    client.Send_Data(un_pwd)

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
    # client = socket.socket()
    # HOST, PORT = "132.198.11.12", 12000
    # client.connect((HOST, PORT))

    data = "AUTH:test1:p001"
    # client.Send_Data(data)
    # while not client.authenticated:
    #     authenticate(client)
    run = True
    while run:
        #menu_options()
        readers, _, _ = select.select([client.s], [], [])
        print(type(readers))
        for reader in readers:
            if reader is client:
                client.Receive()
                print(client.received)
            else:
                i = sys.stdin.readline()
                if i == "exit":
                    run = False
                else:
                    client.Send_Data(i)
            exit()






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
