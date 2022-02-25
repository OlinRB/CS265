import select

"""
Main Loop class for chat.py

Adds readers client and u_input 
listening for either server response
or user input
"""


class Loop():
    def __init__(self):
        self.readers = []

    def Add_Reader(self, reader):
        self.readers.append(reader)

    def Menu(self):
        print("Please choose an option:")
        print("1) List online users")
        print("2) Send a message")
        print("3) Sign off")

    def Run(self):
        # Utilize select to listen for server response
        # and user input
        while True:
            readers, _, _ = select.select(self.readers, [], [])
            for reader in readers:
                reader.Read_Data()
                self.Menu()


