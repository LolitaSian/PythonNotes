# 练习5-1：条件测试 编写一系列条件测试，将每个测试以及对其结果的预测和实际结果打印出来。
# 你编写的代码应类似于下面这样：
print("5-1")
car = 'TOYOTA'
print(car == "TOYOTA")  # true
print(car == 'BWM')     # false

# 练习5-2：更多条件测试
# 对于下面列出的各种情况，至少编写两个结果分别为True和False的测试。
# ❏ 检查两个字符串相等和不等。
# ❏ 使用方法lower()的测试。
# ❏ 涉及相等、不等、大于、小于、大于等于和小于等于的数值测试。
# ❏ 使用关键字and和or的测试。
# ❏ 测试特定的值是否包含在列表中。
# ❏ 测试特定的值是否未包含在列表中。
print("\n5-2")
str1 = "Hello World"
str2 = "HEllo world"
print(str1 == str2)
print(str1 == str2.title())

# 练习5-3：外星人颜色
# 假设在游戏中刚射杀了一个外星人，请创建一个名为alien_color的变量，
# 并将其赋值为'green'、'yellow'或'red'。
# 编写一条if语句，检查外星人是否是绿色的。如果是，就打印一条消息，指出玩家获得了5分。
# 编写这个程序的两个版本，在一个版本中上述测试通过了，而在另一个版本中未通过（未通过测试时没有输出）。
print("\n5-3")
alien_color = 'green'
if alien_color == 'green':
    print("获得5分")

# 练习5-4：外星人颜色2
# 像练习5-3那样设置外星人的颜色，并编写一个if-else结构。
# 如果外星人是绿色的，就打印一条消息，指出玩家因射杀该外星人获得了5分。
# 如果外星人不是绿色的，就打印一条消息，指出玩家获得了10分。
print("\n5-4")
if alien_color == 'green':
    print("获得5分")
else:
    print("获得10分")

# 练习5-5：外星人颜色3
# 将练习5-4中的if-else结构改为if-elif-else结构。
# 如果外星人是绿色的，就打印一条消息，指出玩家获得了5分。
# 如果外星人是黄色的，就打印一条消息，指出玩家获得了10分。
# 如果外星人是红色的，就打印一条消息，指出玩家获得了15分。
print("\n5-5")
if alien_color == 'green':
    print("获得5分")
elif alien_color == 'yello':
    print("获得10分")
else:
    print("获得15分")

# 练习5-6：人生的不同阶段
# 设置变量age的值，再编写一个if-elif-else结构，
# 根据age的值判断一个人处于人生的哪个阶段。
# 如果年龄小于2岁，就打印一条消息，指出这个人是婴儿。
# 如果年龄为2（含）～4岁，就打印一条消息，指出这个人是幼儿。
# 如果年龄为4（含）～13岁，就打印一条消息，指出这个人是儿童。
# 如果年龄为13（含）～20岁，就打印一条消息，指出这个人是青少年。
# 如果年龄为20（含）～65岁，就打印一条消息，指出这个人是成年人。
# 如果年龄超过65岁（含），就打印一条消息，指出这个人是老年人。
print("\n5-6")
age = int(input("请输入年龄："))
if age<2:
    print("婴儿")
elif age>=2 and age<4:
    print("幼儿")
elif age>=4 and age<13:
    print("儿童")
elif age>=13 and age<20:
    print("青少年")
elif age>=20 and age<65:
    print("成年人")
else:
    print("老年人")

# 练习5-7：喜欢的水果
# 创建一个列表，再编写一系列独立的if语句，检查列表中是否包含特定的水果。
# 将该列表命名为favorite_fruits，并在其中包含三种水果。
# 编写5条if语句，每条都检查某种水果是否包含在列表中。
# 如果是，就打印一条消息，You really like bananas!
print("\n5-7")
favorite_fruits = ['apple','peach','watermelon']
count = 5
while count>0:
    fruit = input("输入你喜欢的水果：")
    for i in favorite_fruits:
        if i == fruit:
            print(f"You really like {i}!")
    count -= 1

# 练习5-8：以特殊的方式跟管理员打招呼
# 创建一个至少包含5个用户 的列表，且其中一个用户名为admin。
# 想象你要编写代码，在每位用户登录网站后都打印一条问候消息，如下所示
# 如果管理员登录，打印一条特殊的问候消息
# Hello admin, would you like to see a status report?
# 否则打印一条普通消息
# Hello Sian, thank you for logging in again.
print("\n5-8")
user = ['Ann','admin','Sean','Jack','Lily']
for i in user:
    if i == 'admin':
        print(f"Hello {i}, would you like to see a status report?")
    else:
        print(f"Hello {i},  thank you for logging in again.")

# 练习5-9：处理没有用户的情形
# 给5-8程序添加一条if语句，检查用户名列表是否为空，如果为空，就打印
# We need to find some users!
print("\n5-9")
if user:
    for i in user:
        if i == 'admin':
            print(f"Hello {i}, would you like to see a status report?")
        else:
            print(f"Hello {i},  thank you for logging in again.")
else:
    print("We need to find some users!")

# 练习5-10：检查用户名
# 按下面的说明编写一个程序，模拟网站如何确保每位用户的用户名都独一无二。
# 创建一个至少包含5个用户名的列表，并将其命名为current_users。
# 再创建一个包含5个用户名的列表，将其命名为new_users，并确保其中有一两个用户名也包含在列表current_users中。
# 遍历列表new_users，对于其中的每个用户名，都检查它是否已被使用。
# 如果是，就打印一条消息，指出需要输入别的用户名；
# 否则，打印一条消息，指出这个用户名未被使用。
# 确保比较时不区分大小写。换句话说，如果用户名’John’已被使用，应拒绝用户名’JOHN'。'
# （为此，需要创建列表current_users的副本，其中包含当前所有用户名的小写版本。）
print("\n5-10")
current_users = ['Ann','admin','Sian','Jack','Steven']
new_users = ['Sam','Amy','ADMIN','Sean','Steven']
for i in new_users:
    print(f"Current user is {i}")
    flag = False
    for j in current_users:
        if i == j or i == j.upper() or i == j.lower():
            print("Your name already be used. Please change another name.")
            flag = True
    if flag == False:
        print(f"Hello {i}")

# 练习5-11：序数
# 序数表示位置，如1st和2nd。
# 序数大多以th结尾，只有1、2和3例外。
# 在一个列表中存储数字1～9。
# 遍历这个列表。
# 在循环中使用一个if-elif-else结构，以打印每个数字对应的序数。
# 输出内容应为"1st 2nd3rd 4th 5th 6th 7th 8th 9th"，但每个序数都独占一行。
print("\n5-11")
number = [1,2,3,4,5,6,7,8,9]
for i in number:
    if i == 1:
        print(f"{i}st")
    elif i == 2:
        print(f"{i}nd")
    elif i == 3:
        print(f"{i}rd")
    else:
        print(f"{i}th")


