from model.address import Address

class Person:
    id = None
    name = ""
    addr = ""

    def __init__(self, data):
        self.id = data[0]
        self.name = data[1]
        self.addr = Address(data[4])

