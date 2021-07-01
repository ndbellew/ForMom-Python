
class Customer():

    def __init__(self,name, address):
        self.name = name
        self.address = address

        
    def __str__(self):
        return f"{self.name}\n{str(self.address)}"