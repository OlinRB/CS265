import socket
import sys
import select
from client import Client



def main():
    HOST, PORT = "132.198.11.12", 12000
    client = Client(HOST, PORT)
    while True:
        readers, _, _ = select.select([sys.stdin, client], [], [])
        for reader in readers:
            if reader is client:
                client.Print_Data()
                print(">", end=" ")
            else:
                client.Send_Data()

main()
