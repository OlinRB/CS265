import sys

class Input():
    def __init__(self, client):
        self.client = client

    def fileno(self):
        return sys.stdin.fileno()


    def Read_Data(self):
        self.client.Send_Data()