# 3.11.1 Collatz 序列
# 编写一个名为 collatz()的函数，它有一个名为 number 的参数。
# 如果参数是偶数，那么 collatz()就打印出 number // 2，并返回该值。
# 如果 number 是奇数，collatz()就打印并返回 3 * number + 1。
# 然后编写一个程序，让用户输入一个整数，并不断对这个数调用 collatz()，直到函数返回值１
# （令人惊奇的是，这个序列对于任何整数都有效，你的程序在研究所谓的“Collatz序列”，
# 它有时候被称为“最简单的、不可能的数学问题”）。

# 3.11.2 输入验证
# 在前面的项目中添加 try 和 except 语句，检测用户是否输入了一个非整数的字符串。
# 正常情况下，int()函数在传入一个非整数字符串时，会产生 ValueError 错误，比如 int('puppy')。
# 在 except 子句中，向用户输出一条信息，告诉他们必须输入一个整数。
def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1
try:
    num = int(input("请输入一个数字："))
except ValueError:
    print("请输入整数。")
else:
    flag = False        # 做标记，防止重复输出1
    while num:
        if num == 1:
            if flag == False:
                print(1)
            break
        else:
            flag = True
            num = collatz(num)


# 4.10.1 逗号代码
# 假定有下面这样的列表：
# spam = ['apples', 'bananas', 'tofu', 'cats']
# 编写一个函数，它以一个列表值作为参数，返回一个字符串。
# 该字符串包含所有表项，表项之间以逗号和空格分隔，并在最后一个表项之前插入 and。
# 例如，将 前面的 spam 列表传递给函数，将返回'apples, bananas, tofu, and cats'。
# 但你的函数应该能够处理传递给它的任何列表。
spam = ['apples', 'bananas', 'tofu', 'cats']
def printf(spam):
    for i in spam:
        if i != spam[-1]:
            print(i,end=', ')
        else:
            print('and '+i)
printf(spam)

# 4.10.2 字符图网格
# 假定有一个列表的列表，内层列表的每个值都是包含一个字符的字符串，像这样：
# grid = [['.', '.', '.', '.', '.', '.'],
        # ['.', 'O', 'O', '.', '.', '.'],
        # ['O', 'O', 'O', 'O', '.', '.'],
        # ['O', 'O', 'O', 'O', 'O', '.'],
        # ['.', 'O', 'O', 'O', 'O', 'O'],
        # ['O', 'O', 'O', 'O', 'O', '.'],
        # ['O', 'O', 'O', 'O', '.', '.'],
        # ['.', 'O', 'O', '.', '.', '.'],
        # ['.', '.', '.', '.', '.', '.']]
# 你可以认为 grid[x][y]是一幅“图”在 x、y 坐标处的字符，该图由文本字符组成。
# 原点(0, 0)在左上角，向右 x 坐标增加，向下 y 坐标增加。复制前面的网格值，编写代码用它打印出图像。
# ..OO.OO..
# .OOOOOOO.
# .OOOOOOO.
# ..OOOOO..
# ...OOO...
# ....O....
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
for i in range(0,len(grid[0])):
    for j in range(0,len(grid)):
        print(grid[j][i],end='')
    print()


# 5.6.1 好玩游戏的物品清单
# 你在创建一个好玩的视频游戏。用于对玩家物品清单建模的数据结构是一个字典。
# 其中键是字符串，描述清单中的物品，值是一个整型值，说明玩家有多少该物品。
# 例如，字典值{'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
# 意味着玩家有 1 条绳索、6 个火把、42 枚金币等。
# 写一个名为 displayInventory()的函数，它接受任何可能的物品清单，并显示如下：
# Inventory:
# 12 arrow
# 42 gold coin
# 1 rope
# 6 torch
# 1 dagger
# Total number of items: 62
tool = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
def displayInventory(tools):
    print("Inventory:")
    count = 0
    for k,v in tools.items():
        print(str(v)+" "+k)
        count += v
    print("Total number of items: " + str(count))
displayInventory(tool)

# 5.6.2 列表到字典的函数，针对好玩游戏物品清单
# 假设征服一条龙的战利品表示为这样的字符串列表：
# dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
# 写一个名为 addToInventory(inventory, addedItems)的函数，
# 其中 inventory 参数是一个字典，表示玩家的物品清单（像前面项目一样），
# addedItems 参数是一个列表，就像 dragonLoot。
# addToInventory()函数应该返回一个字典，表示更新过的物品清单。
# 请注意，列表可以包含多个同样的项。你的代码看起来可能像这样：
# def addToInventory(inventory, addedItems):
#       your code goes here
# inv = {'gold coin': 42, 'rope': 1}
# dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
# inv = addToInventory(inv, dragonLoot)
# displayInventory(inv)
# 前面的程序（加上前一个项目中的 displayInventory()函数）将输出如下：
# Inventory:
# 45 gold coin
# 1 rope
# 1 ruby
# 1 dagger
# Total number of items: 48
inv = {'gold coin': 42, 'rope': 1}
displayInventory(inv)
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
def addToInventory(inventory, addedItems):
    for i in addedItems:
        inventory.setdefault(i,0)
        inventory[i] += 1
    return inventory
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)

# 6.7 表格打印
# 编写一个名为 printTable()的函数，它接受字符串的列表的列表，
# 将它显示在组织良好的表格中，每列右对齐。假定所有内层列表都包含同样数目的字符串。
# 例如，该值可能看起来像这样：
# tableData = [['apples', 'oranges', 'cherries', 'banana'],
#             ['Alice', 'Bob', 'Carol', 'David'],
#             ['dogs', 'cats', 'moose', 'goose']]
# 你的 printTable()函数将打印出：
#   apples Alice  dogs
#  oranges   Bob  cats
# cherries Carol moose
#   banana David goose
tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]
def printTable(table):
    for i in range(0,len(table[0])):
        for j in range(0,len(table)):
            print(table[j][i].rjust(8),end=' ')
        print()
printTable(tableData)