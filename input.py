import sys

class Input():
    def __init__(self, client):
        self.client = client

    def fileno(self):
        return sys.stdin.fileno()


    def Read_Data(self):
        print("Please choose an option:")
        print("1) List online users")
        print("2) Send a message")
        print("3) Sign off")
        self.client.Send_Data()