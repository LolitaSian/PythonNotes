# 练习7-1：汽车租赁
# 编写一个程序，询问用户要租赁什么样的汽车，并打印一条消息，
# 下面是一个例子。Let me see if I can find you a Subaru.
print("\n7-1")
car = input("What car do you want?")
print(f"Let me see if I can find you a {car}.")

# 练习7-2：餐馆订位
# 编写一个程序，询问用户有多少人用餐。
# 如果超过8位，就打印一条消息，指出没有空桌；否则指出有空桌。
print("\n7-2")
people = input("How many people want to eat something?")
if int(people)>8:
    print(f"Sorry, we don't have enough tables for {people} persons.")
else:
    print("Welcome")

# 练习7-3：10的整数倍
# print("\n5-11")让用户输入一个数，并指出该数是否是10的整数倍。
print("\n7-3")
num = int(input("请输入一个数："))
if num%10==0:
    print("10的整数倍")
else:
    print("不是10的整数倍")

# 练习7-4：比萨配料
# 编写一个循环，提示用户输入一系列比萨配料，并在用户输入‘quit’时结束循环。
# 每当用户输入一种配料后，都打印一条消息，指出我们会在比萨中添加这种配料。
print("\n7-4")
count = 3
while count>0:
    food = input("请输入一种食材：")
    print(f"我们会在比萨中添加{food}")
    count -= 1

# 练习7-5：电影票
# 有家电影院根据观众的年龄收取不同的票价：
# 不到3岁的观众免费；3～12岁的观众收费10美元；超过12岁的观众收费15美元。
# 请编写一个循环，在其中询问用户的年龄，并指出其票价。
print("\n7-5\n见7-6")

# 练习7-6：三种出路
# 以不同的方式完成练习7-4或练习7-5，在程序中采取如下做法。
# 在while循环中使用条件测试来结束循环。
# 使用变量active来控制循环结束的时机。
# 使用break语句在用户输入‘quit’时退出循环。
print("\n7-6")
while True:
    active =  input("请输入年龄：")
    if active == 'quit':
        break
    else:
        age = int(active)
    if age<3:
        print("Free")
    elif age>=3 and age<=12:
        print("10$")
    else:
        print("15$")

# 练习7-7：无限循环
# 编写一个没完没了的循环，并运行它（要结束该循环，可按Ctrl+ C，也可关闭显示输出的窗口）。
print("\n7-7\n略")

# 练习7-8：熟食店
# 创建一个名为sandwich_orders的列表，在其中包含各种三明治的名字，
# 再创建一个名为finished_sandwiches的空列表。
# 遍历列表sandwich_orders，对于其中的每种三明治，都打印一条消息，
# 如I made your tuna sandwich，并将其移到列表finished_sandwiches中。
# 所有三明治都制作好后，打印一条消息，将这些三明治列出来。
print("\n7-8")
sandwich_orders = ['pastrami','火腿奶酪三明治','pastrami','金枪鱼三明治','肉松三明治','pastrami']
finished_sandwiches = []
for i in sandwich_orders:
    print(f"I made your {i}")
    finished_sandwiches.append(i)
print(finished_sandwiches)


# 练习7-9：五香烟熏牛肉卖完了
# 使用为完成练习7-8而创建的列表sandwich_orders，并确保’pastrami’在其中至少出现了三次。
# 在程序开头附近添加这样的代码：打印一条消息，指出熟食店的五香烟熏牛肉（pastrami）卖完了；
# 再使用一个while循环将列表sandwich_orders中的‘pastrami’都删除。
# 确认最终的列表finished_sandwiches未包含'pastrami'。
print("\n7-9")
print("熟食店的五香烟熏牛肉（pastrami）卖完了")
print(sandwich_orders)
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)