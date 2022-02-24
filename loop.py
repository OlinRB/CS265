import select

class Loop():
    def __init__(self):
        self.readers = []


    def Add_Reader(self, reader):
        self.readers.append(reader)


    def Run(self):
        print("Please choose an option:")
        print("1) List online users")
        print("2) Send a message")
        print("3) Sign off")
        while True:
            readers, _, _ = select.select(self.readers, [], [])
            for reader in readers:
                reader.Read_Data(None)
                print("Please choose an option:")
                print("1) List online users")
                print("2) Send a message")
                print("3) Sign off")

