import socket
import sys
import select

def connect():
    connection = socket.socket()
    HOST, PORT = "132.198.11.12", 12000
    connection.connect((HOST, PORT))
    return connection

def authenticate(connection):
    un = input("Please enter your username: ")
    pwd = input("Please enter your password: ")
    un_pwd = "AUTH:{}:{}".format(un, pwd)
    connection.sendall(bytes(un_pwd + "\n", "utf-8"))
    # print(str(client.s.recv(1024), "utf-8").strip())
    if str(connection.recv(1024), "utf-8").strip() == "AUTHYES":
        return True
def main():
    connection = connect()
    print("Success")
    authenticated = authenticate(connection)
    while not authenticated:
        authenticated = authenticate(connection)

    while True:

        readers,_,_= select.select([sys.stdin,connection],[],[])
        for reader in readers:
            if reader is connection:
                print(connection.recv(1000).decode("utf8"))
            else:
                msg = sys.stdin.readline()
                connection.send(msg.encode("utf8"))

main()