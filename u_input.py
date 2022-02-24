import sys

class Input():
    def __init__(self, client):
        self.client = client

    def fileno(self):
        return sys.stdin.fileno()

    def Menu(self):
        print("\nPlease choose an option:")
        print("1) List online users")
        print("2) Send a message")
        print("3) Sign off")


    def Read_Data(self):
        print("\n")
        self.Menu()
        self.client.Send_Data()