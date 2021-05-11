class Pet:
    def __init__(self,name,type,weight):
        self.name = name
        self.type = type
        self.weight = weight
    def introduce(self):
        print(f"My name is {self.name.title()}.Now I am {self.age} years old.")