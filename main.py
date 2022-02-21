import socketserver

"""
UVMPM cmd line chat interface

servers listening at port: 12000

Handshake->Authentication->Request/Response
Server IP: 132.198.11.12–

"""
from client import Client


HOST, PORT = "132.198.11.12", 12000
data = "HELLO"

client = Client(HOST, PORT)
client.Send_Data(data)
print(client.received)

data = "AUTH:test1:p001"
client.Send_Data(data)
print(client.received)





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
