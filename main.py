import socketserver

"""
UVMPM cmd line chat interface

servers listening at port: 12000

Handshake->Authentication->Request/Response
Server IP: 132.198.11.12–

"""

import socket
from client import Client
import sys

HOST, PORT = "132.198.11.12", 12000
data = "HELLO"

client = Client(HOST, PORT)
client.Send_Data(data)






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
