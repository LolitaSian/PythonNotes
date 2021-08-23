class Person:
    def __init__(self,name):
        self.name = name
        self.age = 18
    def introduce(self):
        print(f"My name is {self.name.title()}.Now I am {self.age} years old.")
    def correct_age(self,num):
        self.age = num
p1 = Person('sian')
p1.introduce()
p1.age = 20         # 通过属性修改属性值
p1.introduce()
p1.correct_age(25)  # 通过方法修改属性值
p1.introduce()

# 继承
class School:
    def __init__(self,stu_school,stu_class):
        self.stu_school = stu_school
        self.stu_class = stu_class
    def show_message(self):
        print(f"School:{self.stu_school},Class:{self.stu_class}")
class Student(Person):
    def __init__(self,name):
        super().__init__(name)
        self.school = School("IMU",'1')     # 类做实例
    def introduce(self):        # 子类父类有同名方法时，子类覆盖掉父类
        print(f"I am {self.name.title()}")
s1 = Student('Sean')
s1.introduce()
s1.school.show_message()

import i_import2  # 这样导入就把i_import2看做一个对象
p1 = i_import2.Dog('刘姐姐','狗','40')
p1.set_age()
p1.introduce()

from i_import2 import Dog
p2 = Dog('刘贱贱','狗','20')
p2.set_age()
p2.introduce()

from i_import2 import Cat as mimi # 这样导入直接使用import_demo_09中的对象
p3 = mimi('刘妹妹','猫','8','狸花猫')
p3.introduce()
p4 = mimi('刘弟弟','猫','1','奶牛猫')
p4.introduce()
# from file import * 可以导入某一模板文件中所有的类，但是不建议使用，容易混淆其中的类有哪些
