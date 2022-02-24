import select

class Loop():
    def __init__(self):
        self.readers = []


    def Add_Reader(self, reader):
        self.readers.append(reader)


    def Run(self):
        while True:
            readers, _, _ = select.select(self.readers, [], [])
            for reader in readers:
                reader.Read_Data()

