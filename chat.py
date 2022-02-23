import socket
import sys
import select
from client import Client
from loop import Loop
from input import Input



def main():
    HOST, PORT = "132.198.11.12", 12000
    client = Client(HOST, PORT)
    client.Init_Connection()
    input = Input(client)
    while not client.authenticated:
        client.Authenticate()
    connection = Loop()
    connection.Add_Reader(client)
    connection.Add_Reader(input)
    connection.Run()


main()
