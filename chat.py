import socket
import sys
import select
from client import Client
from socket_connection import Socket_Connection
from input import Input


def main():
    HOST, PORT = "132.198.11.12", 12000
    client = Client(HOST, PORT)
    input = Input(client)
    connection = Socket_Connection()
    connection.Add_Reader(client)
    connection.Add_Reader(input)
    connection.Run()


main()
