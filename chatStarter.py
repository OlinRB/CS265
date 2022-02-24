import socket
import sys
import select

def main():
    oop = False
    if oop:
        client = socket.socket()
        HOST, PORT = "132.198.11.12", 12000
        client.connect((HOST, PORT))
        while True:
            readers, _, _ = select.select([sys.stdin, client], [], [])
            for reader in readers:
                if reader is client:
                    print(str(client.recv(1024), "utf-8"))
                    print(">", end=" ")
                else:
                    data = sys.stdin.readline()
                    client.send(data.encode("utf-8"))
    else:
        HOST, PORT = "132.198.11.12", 12000
        s = socket.socket()
        s.connect((HOST, PORT))
        data = "HELLO\n".encode("utf-8")
        s.send(data)
        response = str(s.recv(1024), "utf-8")
        print(response)
main()
