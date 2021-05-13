# 练习10-1:Python学习笔记
# 在文本编辑器中新建一个文件，写几句话来总结一下你至此学到的Python知识，
# 其中每一行都以“In Python you can”打头。
# 将这个文件命名为learning_python.txt，并存储到为完成本章练习而编写的程序所在的目录中。
# 编写一个程序，它读取这个文件，并将你所写的内容打印三次：
# 第一次打印时读取整个文件；
# 第二次打印时遍历文件对象；
# 第三次打印时将各行存储在一个列表中，
# 再在with代码块外打印它们。
print("\n10-1")
with open('j_file/10-1 learning_python.txt') as F1:
    contents = F1.read()
print(contents)

with open ('j_file/10-1 learning_python.txt') as F1:
    for line in F1:
        print(line.rstrip())

with open ('j_file/10-1 learning_python.txt') as F1:
    lines = F1.readlines()
for line in lines:
    print(line.rstrip())

# 练习10-2:C语言学习笔记
# 可使用方法replace()将字符串中的特定单词都替换为另一个单词。
# 下面是一个简单的示例，演示了如何将句子中的’dog’替换为’cat'：
print("\n10-2")
with open ('j_file/10-1 learning_python.txt') as F2:
    lines = F2.readlines()
for line in lines:
    line = line.replace('Python','C++')
    print(line.rstrip())

# 练习10-3：访客
# 编写一个程序，提示用户输入名字。用户做出响应后，将其名字写入文件guest.txt中。
print("\n10-3")
with open('j_file/10-3 guest.txt','w') as F3:
    name = input("请输入访客姓名：")
    F3.write(name)

# 练习10-4：访客名单
# 编写一个while循环，提示用户输入名字。用户输入名字后，在屏幕上打印一句问候语，
# 并将一条到访记录添加到文件guest_book.txt中。确保这个文件中的每条记录都独占一行。
print("\n10-4")
print("输入q随时退出。")
with open('j_file/10-4 guest_book.txt','a') as F4:
    while True:
        name = input("请输入访客姓名：")
        if name == 'q':
            break
        F4.write(name+'\n')

# 练习10-5：调查
# 编写一个while循环，询问用户为何喜欢编程。
# 每当用户输入一个原因后，都将其添加到一个存储所有原因的文件中。
print("\n10-5")
print("输入q随时退出。")
with open('j_file/10-5 reasons.txt','a') as F5:
    while True:
        reason = input("Why do you like programming：")
        if reason == 'q':
            break
        F5.write(reason+'\n')

# 练习10-6：加法运算
# 提示用户提供数值输入时，常出现的一个问题是，用户提供的是文本而不是数。
# 在此情况下，当你尝试将输入转换为整数时，将引发ValueError异常。
# 编写一个程序，提示用户输入两个数，再将其相加并打印结果。
# 在用户输入的任何一个值不是数时都捕获ValueError异常，并打印一条友好的错误消息。
# 对你编写的程序进行测试：先输入两个数，再输入一些文本而不是数。
print("\n10-6")

# 练习10-7：加法计算器
# 将为完成练习10-6而编写的代码放在一个while循环中，
# 让用户犯错（输入的是文本而不是数）后能够继续输入数。
print("\n10-7")
print("Give me 2 numbers,and I will add them.")
print("You can enter 'q' to quit.")
while True:
    a = input("First number:")
    if a == 'q':
        break
    b = input("Second number:")
    if b == 'q':
        break
    try:
        answer = int(a)+int(b)
    except ValueError:       # 这样出现异常就不会终止程序的运行
        print("你输入的不是数字！")
    else:
        print(answer)

# 练习10-8：猫和狗
# 创建文件cats.txt和dogs.txt，
# 在第一个文件中至少存储三只猫的名字，在第二个文件中至少存储三条狗的名字。
# 编写一个程序，尝试读取这些文件，并将其内容打印到屏幕上。
# 将这些代码放在一个try-except代码块中，以便在文件不存在时捕获FileNotFound错误，
# 并显示一条友好的消息。将任意一个文件移到另一个地方，并确认except代码块中的代码将正确执行。
print("\n10-8")
files = ['j_file/10-8 cat.txt','/10-8 dog.txt'] # 第二个文件名是错的
for i in files:
    try:
        with open(i) as File:
            contents = File.read()
    except FileNotFoundError:
        print(f"找不到{i}！")
    else:
        print(contents)

# 练习10-9：静默的猫和狗
# 修改你在练习10-8中编写的except代码块，让程序在任意文件不存在时静默失败。
print("\n10-9")
files = ['j_file/10-8 cat.txt','/10-8 dog.txt'] # 第二个文件名是错的
for i in files:
    try:
        with open(i) as File:
            contents = File.read()
    except FileNotFoundError:
        pass
    else:
        print(contents)

# 练习10-10：常见单词
# 访问古登堡计划，找一些你想分析的图书。
# 下载这些作品的文本文件或将浏览器中的原始文本复制到文本文件中。
# 就用爱丽丝那一篇吧
print("\n10-10")
with open('j_file/10 Alice.txt') as Alice:
    contents = Alice.read()
print(contents.lower().count('the'))

# 练习10-11：喜欢的数
# 编写一个程序，提示用户输入喜欢的数，并使用json.dump()将这个数存储到文件中。
# 再编写一个程序，从文件中读取这个值，并打印如下所示的消息。
# I know your favorite number! It's _____.
print("\n10-11")
import json
with open('j_file/10-11 favorite_number.json','w') as F11:
    num = input("请输入喜欢的数：")
    json.dump(num,F11)
with open('j_file/10-11 favorite_number.json') as F11:
    num = json.load(F11)
    print(f"I know your favorite number! It's {num}.")

# 练习10-12：记住喜欢的数
# 将练习10-11中的程序合二为一。如果存储了用户喜欢的数，就向用户显示它，
# 否则提示用户输入喜欢的数并将其存储到文件中。运行这个程序两次，看看它能否像预期的那样工作。
print("\n10-12")
import json
try:
    with open('j_file/10-12 favorite_number.json') as F11:
        num = json.load(F11)
except FileNotFoundError:
    with open('j_file/10-12 favorite_number.json', 'w') as F11:
        num = input("请输入喜欢的数：")
        json.dump(num, F11)
else:
    print(f"I know your favorite number! It's {num}.")

# 练习10-13：验证用户
# 最后一个remember_me.py版本假设用户要么已输入用户名，要么是首次运行该程序。
# 我们应该修改这个程序，以防当前用户并非上次运行该程序的用户。
# 为此，在greet_user()中打印欢迎用户回来的消息前，询问他用户名是否正确。
# 如果不对，就调用get_new_username()让用户输入正确的用户名。
print("\n10-13")
import json
def get_stored_name():
    try:
        with open('j_file/10-13 user.json') as F13:
            username = json.load(F13)
    except FileNotFoundError:
        return None
    else:
        return username
def get_new_username():
    username = input("请输入用户名：")
    with open("j_file/10-13 user.json",'w') as F13:
        json.dump(username,F13)
    return username
def greet_user():
    username = get_stored_name()
    if username:
        print(f"Are you {username}?")
        flag = input("Enter 'y' for Yes 'n' for No")
        if flag == 'y':
            print(f"Welcome back {username}!")
        else:
            username = get_new_username()
            print(f"We will remember you when you come back,{username}.")
    else:
        username = get_new_username()
        print(f"We will remember you when you come back,{username}.")
greet_user()