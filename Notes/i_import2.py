from i_import1 import Pet
class Dog(Pet):
    def __init__(self,name,type,weight):
        super(Dog, self).__init__(name,type,weight)
        self.age = ''
    def set_age(self):
        self.age = input(f"请输入{self.name}的年龄:")
    def introduce(self):
        print(f"{self.name}，重{self.weight}斤，已经{self.age}岁了。")

class Cat(Pet):
    def __init__(self,name,type,weight,breed):
        super(Cat, self).__init__(name,type,weight)
        self.breed = breed
    def introduce(self):
        print(f"{self.name}，是一只{self.breed}，重{self.weight}斤。")