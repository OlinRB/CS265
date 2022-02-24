from client import Client
from loop import Loop
from u_input import Input

"""
Program creates connection to server using
client object. Client object and u_input
object added to loop object for continuous 
connection to specified server.

"""



def main():
    HOST, PORT = "132.198.11.12", 12000
    HOST = input("Please enter the server address: ")
    PORT = int(input("PLEASE enter the server port: "))
    client = Client(HOST, PORT)
    while not client.authenticated:
        client.Authenticate()
    u_input = Input(client)
    connection = Loop()
    connection.Add_Reader(client)
    connection.Add_Reader(u_input)
    connection.Run()


main()
