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
    # Get host and port number from user
    HOST = input("Please enter the server address: ")
    PORT = input("Please enter the server port: ")
    while not PORT.isalnum():
        print("Error: invalid port number")
        PORT = input("Please enter the server port: ")
    PORT = int(PORT)
    # Initialize connection
    client = Client(HOST, PORT)
    # Authenticate user
    while not client.authenticated:
        client.Authenticate()
    # Initialize input reader
    u_input = Input(client)
    # Initialize loop
    connection = Loop()
    # Add connection and input reader to loop
    connection.Add_Reader(client)
    connection.Add_Reader(u_input)
    # Run loop
    connection.Run()


main()
