import sys

"""
Input class calls client.py object
input function to user input using
stdin
"""


class Input():
    def __init__(self, client):
        self.client = client

    def fileno(self):
        return sys.stdin.fileno()

    def Read_Data(self):
        # Call clients input data function
        print("\n")
        self.client.Send_Data()