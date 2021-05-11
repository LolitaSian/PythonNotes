# 练习4-1：比萨
# 想出至少三种你喜欢的比萨，将其名称存储在一个列表中，再使用for循环将每种比萨的名称打印出来。
# ❏ 修改这个for循环，使其打印包含比萨名称的句子，而不仅仅是比萨的名称。
# 对于每种比萨，都显示一行输出，下面是一个例子。
# I like pepperoni pizza.
# ❏ 在程序末尾添加一行代码，它不在for循环中，指出你有多喜欢比萨。
# 输出应包含针对每种比萨的消息，还有一个总结性句子，下面是一个例子。
# I really love pizza!
print("4-1:")
pizza = ['p1','p2','p3']
for p in pizza:
    print(f"I like {p}.")
print("I really love pizza!")

# 练习4-2：动物
# 想出至少三种有共同特征的动物，将其名称存储在一个列表中，再使用for循环将每种动物的名称打印出来。
# ❏ 修改这个程序，使其针对每种动物都打印一个句子，下面是一个例子。
# A dog would make a great pet.
# ❏ 在程序末尾添加一行代码，指出这些动物的共同之处，如打印下面这样的句子。
# Any of these animals would make a great pet!
print("\n4-2:")
pets = ['cat','dog','parrot']
for pet in pets:
    print(f"A {pet} would make a great pet.")
print("Any of these animals would make a great pet!")

# 练习4-3：数到20
# 使用一个for循环打印数1～20（含）。
print("\n4-3:")
n20 = range(1,21)
for i in n20:
    print(i,end=' ')

# 练习4-4：一百万
# 创建一个包含数1～1000000的列表，再使用一个for循环将这些数打印出来。
# （如果输出的时间太长，按Ctrl+ C停止输出或关闭输出窗口。）
print("\n4-4:\n略")

# 练习4-5：一百万求和
# 创建一个包含数1～1000000的列表，再使用min()和max()核实该列表确实是从1开始、到1000000结束的。
# 另外，对这个列表调用函数sum()，看看Python将一百万个数相加需要多长时间。
print("\n4-5:")
n1000000 = range(1,1000001)
print(min(n1000000))
print(max(n1000000))
print(sum(n1000000))

# 练习4-6：奇数
# 通过给函数range()指定第三个参数来创建一个列表，其中包含1～20的奇数，
# 再使用一个for循环将这些数打印出来。
print("\n4-6:")
odd = range(1,21,2)
for i in odd:
    print(i,end=' ')

# 练习4-7：3的倍数
# 创建一个列表，其中包含3～30能被3整除的数，再使用一个for循环将这个列表中的数打印出来。
print("\n4-7:")
n3 = range(3,31,3)
for i in n3:
    print(i,end=' ')

# 练习4-8：立方
# 将同一个数乘三次称为立方。例如，在Python中，2的立方用2**3表示。
# 请创建一个列表，其中包含前10个整数（1～10）的立方，再使用一个for循环将这些立方数打印出来。
print("\n4-8:")
cube1 = range(1,11)
for c in cube1:
    c = c**3
    print(c,end=' ')

print("\n")
cube2 = []
for c in range(1,11):
    res = c**3
    cube2.append(res)
print(cube2)

# 练习4-9：立方解析
# 使用列表解析生成一个列表，其中包含前10个整数的立方。
print("\n4-9:")
cube3 = [c**3 for c in range(1,10**3+1)]
print(cube3)


#list复制
l1 = [1,2,3]
l2 = l1     # 浅拷贝
l3 = l1[:]  # 深拷贝
print(l1,l2,l3)
l2.append(4)
l3.append(5)
print(l1,l2,l3)


# 练习4-10：切片
# 选择你在本章编写的一个程序，在末尾添加几行代码，以完成如下任务。
# ❏ 打印消息“The first three items in the list are:”，再使用切片来打印列表的前三个元素。
# ❏ 打印消息“Three items from the middle of the list are:”，再使用切片来打印列表的中间三个元素。
# ❏ 打印消息“The last three items in the list are:”，再使用切片来打印列表的末尾三个元素。
'''
range() 第一个参数起始地址，第二个参数终止地址，第三个参数步长
切片 [:] 第一个参数起始地址，第二个参数终止地址
    [0:3]/[:3] 0到2
    [1:5] 1到4
    [2,-2] 2到 倒数第3个
    [-2:] 最后两个
'''
print("\n4-10:")
num = range(1,20)
for i in num:
    print(i,end=' ')
print("\nThe first three items in the list are:")
for i in num[:3]:
    print(i,end=' ')
print("\nThree items from the middle of the list are:")
f = len(num)//2
for i in num[f-1:-2]:
    print(i,end=' ')
print("\nThe last three items in the list are:")
for i in num[-3:]:
    print(i,end=' ')


# 练习4-11：你的比萨，我的比萨
# 在你为完成练习4-1而编写的程序中，创建比萨列表的副本，并将其赋给变量friend_pizzas，再完成如下任务。
# ❏ 在原来的比萨列表中添加一种比萨。
# ❏ 在列表friend_pizzas中添加另一种比萨。
# ❏ 核实有两个不同的列表。为此，打印消息“My favorite pizzas are:”，
# 再使用一个for循环来打印第一个列表；打印消息“My friend's favorite pizzas are:”，
# 再使用一个for循环来打印第二个列表。核实新增的比萨被添加到了正确的列表中。
print("\n4-11:")
# 4-1中有个pizza = ['p1','p2','p3']
my_pizza = pizza[:]
print("my_pizza = ",my_pizza)
friend_pizza = pizza[:]
print("friend_pizza = ",friend_pizza)

pizza.append('p4')
friend_pizza.append('p5')
print("pizza = ",pizza)
print("my_pizza = ",my_pizza)
print("friend_pizza = ",friend_pizza)


# 练习4-12：使用多个循环
# 在本节中，为节省篇幅，程序foods.py的每个版本都没有使用for循环来打印列表。
# 请选择一个版本的foods.py，在其中编写两个for循环，将各个食品列表打印出来。
print("\n4-12:\n略")


'''
元组dimensions
严格地说，元组是由逗号标识的，圆括号只是让元组看起来更整洁、更清晰。
如果你要定义只包含一个元素的元组，必须在这个元素后面加上逗号： d = (1,)
创建只包含一个元素的元组通常没有意义，但自动生成的元组有可能只有一个元素。
虽然不能修改元组的元素，但是可以给整个元组重新赋值
'''

# 练习4-13：自助餐
# 有一家自助式餐馆，只提供五种简单的食品。请想出五种简单的食品，并将其存储在一个元组中。
# ❏ 使用一个for循环将该餐馆提供的五种食品都打印出来。
# ❏ 尝试修改其中的一个元素，核实Python确实会拒绝你这样做。
# ❏ 餐馆调整了菜单，替换了它提供的其中两种食品。
# 请编写一个这样的代码块：给元组变量赋值，并使用一个for循环将新元组的每个元素都打印出来。
print("\n4-13:")
food = ('f1','f2','f3','f4','f5')
for f in food:
    print(f,end=' ')
# food[2] = 'f6' 会报错
food = ('f1','f2','f3','f7','f8')
print("\n")
for f in food:
    print(f,end=' ')
