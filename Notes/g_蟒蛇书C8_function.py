def function(xc1,xc2):
    print(xc1 + xc2)
function('a','b')           # 位置实参，用传入位置来决定参数
function('b','a')
function(xc2='b',xc1='a')   # 关键字实参，传入实参名值对，打乱顺序也无所谓
def function2(xc1='c',xc2='d'):
    print(xc1 + xc2)
function2('a','b')           # 默认实参，不传入参数也可以
function2('a')           # 默认实参，不传入参数也可以
function2(xc2='a')           # 默认实参，不传入参数也可以
function2()           # 默认实参，不传入参数也可以

# 练习8-1：消息
# 编写一个名为display_message()的函数，它打印一个句子，指出你在本章学的是什么。
# 调用这个函数，确认显示的消息正确无误。
print("8-1:")
def display_message():
    print("I am  learning function.")
display_message()

# 练习8-2：喜欢的图书
# 编写一个名为favorite_book()的函数，其中包含一个名为title的形参。
# 这个函数打印一条消息，下面是一个例子。
# One of my favorite books is Alice in Wonderland.
# 调用这个函数，并将一本图书的名称作为实参传递给它。
print("\n8-2:")
def favorite_book(title):
    print(f"One of my favorite books is {title}.")
favorite_book("Python编程：入门到实践")

# 练习8-3：T恤
# 编写一个名为make_shirt()的函数，它接受一个尺码以及要印到T恤上的字样。
# 这个函数应打印一个句子，概要地说明T恤的尺码和字样。
print("\n8-3:")
def make_shirt(size,character):
    print(f"The size is {size}.")
    print(f"We will print '{character}' on it.")
make_shirt('L','hello world')

# 练习8-4：大号T恤
# 修改函数make_shirt()，使其在默认情况下制作一件印有“I love Python”字样的大号T恤。
# 调用这个函数来制作：一件印有默认字样的大号T恤，一件印有默认字样的中号T恤，
# 以及一件印有其他字样的T恤（尺码无关紧要）。
print("\n8-4:")
def make_shirt(size,character='I love Python'):     # 直接在形参中声明默认值
    print(f"The size is {size}.")
    print(f"We will print '{character}' on it.")
make_shirt('L')
make_shirt('M')
make_shirt('S','hhh')

# 练习8-5：城市
# 编写一个名为describe_city()的函数，它接受一座城市的名字以及该城市所属的国家。
# 这个函数应打印一个简单的句子，下面是一个例子。
# Reykjavik is in Iceland.给用于存储国家的形参指定默认值。
# 为三座不同的城市调用这个函数，且其中至少有一座城市不属于默认国家。
print("\n8-5:")
def describe_city(city,country='China'):
    print(f"{city.title()} is in {country.title()}")
describe_city('beijing')
describe_city('shanghai')
describe_city('Tokyo','japan')

# 练习8-6：城市名
# 编写一个名为city_country()的函数，它接受城市的名称及其所属的国家。
# 这个函数应返回一个格式类似于下面的字符串：
# 至少使用三个城市国家对来调用这个函数，并打印它返回的值。
print("\n8-6:")
def city_country(city,country):
    return f'"{city.title()},{country.title()}"'
print(city_country('shanghai','China'))

# 练习8-7：专辑
# 编写一个名为make_album()的函数，它创建一个描述音乐专辑的字典。
# 这个函数应接受歌手的名字和专辑名，并返回一个包含这两项信息的字典。
# 使用这个函数创建三个表示不同专辑的字典，并打印每个返回的值，
# 以核实字典正确地存储了专辑的信息。
# 给函数make_album()添加一个默认值为None的可选形参，以便存储专辑包含的歌曲数。
# 如果调用这个函数时指定了歌曲数，就将该值添加到表示专辑的字典中。
# 调用这个函数，并至少在一次调用中指定专辑包含的歌曲数。
print("\n8-7:")
def make_album(singer,album,num=''):        # 可选形参放最后，设一个空字符串
        return {'singer':singer,'album':album,'songs':num}
print(make_album('s', 'd', '5'))
print(make_album('q', 'w', '85'))
print(make_album('w', 'd'))

# 练习8-8：用户的专辑
# 在为完成练习8-7编写的程序中，编写一个while循环，让用户输入专辑的歌手和名称。
# 获取这些信息后，使用它们来调用函数make_album()并将创建的字典打印出来。
# 在这个while循环中，务必提供退出途径。
print("\n8-8:")
def make_album2():
    while True:
        singer = input("请输入歌手：")
        if singer == 'quit':
            break
        album = input("请输入专辑：")
        print({'singer':singer,'album':album})
make_album2()

# 练习8-9：消息
# 创建一个列表，其中包含一系列简短的文本消息。
# 将该列表传递给一个名为show_messages()的函数，
# 这个函数会打印列表中的每条文本消息。
print("\n8-9:")
mes = ['hello','world']
def show_messages(text):
    for i in text:
        print(i.title(),end=' ')
show_messages(mes)

# 练习8-10：发送消息
# 在你为完成练习8-9而编写的程序中，编写一个名为send_messages()的函数，
# 将每条消息都打印出来并移到一个名为sent_messages的列表中。
# 调用函数send_messages()，再将两个列表都打印出来，确认正确地移动了消息。
print("\n8-10:")
mes = ['hello','world']
mes_copy = []
def send_messages(mes,text):
    mes.append(text)
def show_messages2(mes1,mes2):
    while mes1:
        current = mes1.pop()
        print(current)
        send_messages(mes2,current)
show_messages2(mes,mes_copy)
print(mes_copy)

# 练习8-11：消息归档
# 修改你为完成练习8-10而编写的程序，在调用函数send_messages()时，向它传递消息列表的副本。
# 调用函数send_messages()后，将两个列表都打印出来，确认保留了原始列表中的消息。
print("\n8-11:")
mes = ['hello','world']
mes_copy = []
def send_messages2(mes,text):
    mes.append(text)
def show_messages3(mes1,mes2):
    while mes1:
        current = mes1.pop(0)   # 设定弹出位置，保证mes和mes_copy的顺序一致
        print(current)
        send_messages(mes2,current)
show_messages3(mes[:],mes_copy)
print(mes)
print(mes_copy)

