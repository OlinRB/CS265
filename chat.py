import socket
import sys
import select

def main():
    client = socket.socket()
    HOST, PORT = "132.198.11.12", 12000
    client.connect((HOST, PORT))
    while True:
        readers, _, _ = select.select([sys.stdin, client], [], [])
        for reader in readers:
            if reader is client:
                print(client.recv(1024), "utf-8")
            else:
                data = sys.stdin.readline()
                client.send(data.encode("utf-8"))

main()
