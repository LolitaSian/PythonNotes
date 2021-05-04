# 练习9-1：餐馆
# 创建一个名为Restaurant的类，为其方法__init__()设置属性restaurant_name和cuisine_type。
# 创建一个名为describe_restaurant()的方法和一个名为open_restaurant()的方法，
# 前者打印前述两项信息，而后者打印一条消息，指出餐馆正在营业。
# 根据这个类创建一个名为restaurant的实例，分别打印其两个属性，再调用前述两个方法。
print("9-1")
class Restaurant1:
    def __init__(self,restaurant_name,cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
    def describe_restaurant(self):
        print(f"Name:{self.name} \ttype:{self.type}")
    def open_restaurant(self):
        print("open!")
r1 = Restaurant1("旺德福","中餐")
r1.open_restaurant()
r1.describe_restaurant()


# 练习9-2：三家餐馆
# 根据为完成练习9-1而编写的类创建三个实例，并对每个实例调用方法describe_restaurant()。
print("\n9-2")
r2 = Restaurant1("France","法餐")
r3 = Restaurant1("Japanese","日料")
r1.describe_restaurant()
r2.describe_restaurant()
r3.describe_restaurant()

# 练习9-3：用户
# 创建一个名为User的类，其中包含属性first_name和last_name，以及用户简介通常会存储的其他几个属性。
# 在类User中定义一个名为describe_user()的方法，用于打印用户信息摘要。
# 再定义一个名为greet_user()的方法，用于向用户发出个性化的问候。
# 创建多个表示不同用户的实例，并对每个实例调用上述两个方法。
print("\n9-3")
class User3:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def describe_user(self):
        print(f"{self.first_name.title()} {self.last_name.title()} is {self.age} years old.")
    def greet_user(self):
        print(f"hello {self.first_name.title()} {self.last_name.title()}")

u1 = User3("Tom","White",17)
u2 = User3("Tim","brown",18)
u1.describe_user()
u2.describe_user()
u1.greet_user()
u2.greet_user()

# 练习9-4：就餐人数
# 在为完成练习9-1而编写的程序中，添加一个名为number_served的属性，并将其默认值设置为0。
# 根据这个类创建一个名为restaurant的实例。打印有多少人在这家餐馆就餐过，然后修改这个值并再次打印它。
# 添加一个名为set_number_served()的方法，让你能够设置就餐人数。
# 调用这个方法并向它传递一个值，然后再次打印这个值。
# 添加一个名为increment_number_served()的方法，让你能够将就餐人数递增。
# 调用这个方法并向它传递一个这样的值：你认为这家餐馆每天可能接待的就餐人数。
print("\n9-4")
class Restaurant4:
    def __init__(self,restaurant_name,cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print(f"Name:{self.name} \ttype:{self.type} \tconsumer:{self.number_served}")
    def open_restaurant(self):
        print("open!")
    def set_number_served(self):
        num = input("请设置就餐人数：")
        self.number_served = int(num)
    def increment_number_served(self,num):
        self.number_served += num
resturant = Restaurant4("旺德福","中餐")
resturant.describe_restaurant()
resturant.set_number_served()
resturant.describe_restaurant()
resturant.increment_number_served(50)
resturant.describe_restaurant()

# 练习9-5：尝试登录次数
# 在为完成练习9-3而编写的User类中，添加一个名为login_attempts的属性。
# 编写一个名为increment_login_attempts()的方法，将属性login_attempts的值加1。
# 再编写一个名为reset_login_attempts()的方法，将属性login_attempts的值重置为0。
# 根据User类创建一个实例，再调用方法increment_login_attempts()多次。
# 打印属性login_attempts的值，确认它被正确地递增。
# 然后，调用方法reset_login_attempts()，并再次打印属性login_attempts的值，确认它被重置为0。
print("\n9-5")
class User5:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0
    def describe_user(self):
        print(f"login_attempts:{self.login_attempts}")
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0
u2 = User5("Tom","White",17)
u2.describe_user()
u2.increment_login_attempts()
u2.describe_user()
u2.increment_login_attempts()
u2.increment_login_attempts()
u2.describe_user()
u2.reset_login_attempts()
u2.describe_user()

# 练习9-6：冰激凌小店
# 冰激凌小店是一种特殊的餐馆。编写一个名为IceCreamStand的类，让它继承为完成练习9-1或
# 练习9-4而编写的Restaurant类。这两个版本的Restaurant类都可以，挑选你更喜欢的那个即可。
# 添加一个名为flavors的属性，用于存储一个由各种口味的冰激凌组成的列表。
# 编写一个显示这些冰激凌的方法。创建一个IceCreamStand实例，并调用这个方法。
print("\n9-6")
class Restaurant6:
    def __init__(self,restaurant_name,cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print(f"Name:{self.name} \ttype:{self.type} \tconsumer:{self.number_served}")
class IceCreamStand(Restaurant6):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = ['chocolate','Vanilla','NEKOPARA']
    def describe_restaurant(self):      # 子类重写父类方法
        print(f"We have {len(self.flavors)} flavors:")
        for i in self.flavors:
            print(i.title())
ics = IceCreamStand("bal",'ice')
ics.describe_restaurant()

# 练习9-7：管理员
# 管理员是一种特殊的用户。编写一个名为Admin的类，让它继承为完成练习9-3或练习9-5而编写的User类。
# 添加一个名为privileges的属性，用于存储一个由字符串
# （如"canadd post"、"can delete post"、"can ban user"等）组成的列表。
# 编写一个名为show_privileges()的方法，显示管理员的权限。
# 创建一个Admin实例，并调用这个方法。
print("\n9-7")
class User7:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def describe_user(self):
        print(f"{self.first_name.title()} {self.last_name.title()} is {self.age} years old.")
class Admin7(User7):
    def __init__(self,first_name,last_name,age):
        super(Admin7, self).__init__(first_name,last_name,age)
        self.privileges = ["can add post","can delete post","can ban user"]
    def show_privileges(self):     # 创建子类自己的方法
        for i in self.privileges:
           print(i)
u3 = Admin7('Q','W',15)
u3.describe_user()
u3.show_privileges()

# 练习9-8：权限
# 编写一个名为Privileges的类，它只有一个属性privileges，其中存储了练习9-7所述的字符串列表。
# 将方法show_privileges()移到这个类中。在Admin类中，将一个Privileges实例用作其属性。
# 创建一个Admin实例，并使用方法show_privileges()来显示其权限。
print("\n9-8")
class Privileges:
    def __init__(self):
        self.privileges = ["can add post","can delete post","can ban user"]
    def show_privileges(self):
        for i in self.privileges:
            print(i)
class User8:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def describe_user(self):
        print(f"{self.first_name.title()} {self.last_name.title()} is {self.age} years old.")
class Admin8(User8):
    def __init__(self,first_name,last_name,age):
        super(Admin8, self).__init__(first_name,last_name,age)
        self.privilege = Privileges()
u4 = Admin8('E','R',16)
u4.describe_user()
u4.privilege.show_privileges()

# 练习9-9：电瓶升级
# 在本节最后一个electric_car.py版本中，给Battery类添加一个名为upgrade_battery()的方法。
# 该方法检查电瓶容量，如果不是100，就将其设置为100。
# 创建一辆电瓶容量为默认值的电动汽车，调用方法get_range()，然后对电瓶进行升级，
# 并再次调用get_range()。你将看到这辆汽车的续航里程增加了。
print("\n9-9")

# 练习9-13：骰子
# 创建一个Die类，它包含一个名为sides的属性，该属性的默认值为6。
# 编写一个名为roll_die()的方法，它打印位于1和骰子面数之间的随机数。
# 创建一个6面的骰子再掷10次。创建一个10面的骰子和一个20面的骰子，再分别掷10次。
print("\n9-10")
import random
class Die:
    def __init__(self,side = 6):
        self.sides = side
    def roll_die(self,num):
        print(f"{self.sides}面骰子投十次：")
        for i in range(num):
            print(f"第{i}次投出的点数为："+ str(random.randint(1,self.sides)))
t6 = Die()
t6.roll_die(10)
t10 = Die(10)
t20 = Die(20)
t10.roll_die(10)
t20.roll_die(10)

# 练习9-14：彩票
# 创建一个列表或元组，其中包含10个数和5个字母。
# 从这个列表或元组中随机选择4个数或字母，并打印一条消息，指出只要彩票上是这4个数或字母，就中大奖了。
from random import choice
character = ['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e']
str = ''
for i in range(4):
    str += choice(character)
print(f"彩票上是{str}就中大奖了")

# 练习9-15：彩票分析
# 可以使用一个循环来明白前述彩票大奖有多难中奖。
# 为此，创建一个名为my_ticket的列表或元组，再编写一个循环，不断地随机选择数或字母，直到中大奖为止。
# 请打印一条消息，报告执行循环多少次才中了大奖。
count = 0
while True:
    str2 = choice(character) + choice(character) + choice(character) + choice(character)
    if str2 == str:
        break
    count += 1
print(count)

# 练习9-16：Python Module of the Week
# 要了解Python标准库，一个很不错的资源是网站Python Module of the Week。
# 请访问该网站并查看其中的目录，找一个你感兴趣的模块进行探索。从模块random开始可能是个不错的选择。
