import socket

class Client:
    def __init__(self, HOST, PORT):
        self.state = "pending"
        self.HOST = HOST
        self.PORT = PORT
        self.Init_Connection()

    def Init_Connection(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.sock:
            # Connect to server and send data
            self.sock.connect((self.HOST, self.PORT))

    def Send_Data(self, message):

        self.sock.sendall(bytes(message + "\n", "utf-8"))

        # Receive data from the server and shut down
        received = str(self.sock.recv(1024), "utf-8")

        print("Sent:     {}".format(message))
        print("Received: {}".format(received))
