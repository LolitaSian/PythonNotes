# 练习6-1：人
# 使用一个字典来存储一个熟人的信息，包括名、姓、年龄和居住的城市。
# 该字典应包含键first_name、last_name、age和city。
# 将存储在该字典中的每项信息都打印出来。
print("6-1")
person = {'first_name':'Sian','last_name':'Lau','age':'18','city':'Yantai'}
for key,value in person.items():
    print('key:\t' + key)
    print('value:\t' + value)

# 练习6-2：喜欢的数
# 使用一个字典来存储一些人喜欢的数。
# 请想出5个人的名字，并将这些名字用作字典中的键；
# 找出每个人喜欢的一个数，并将这些数作为值存储在字典中。
# 打印每个人的名字和喜欢的数。为了让这个程序更有趣，通过询问朋友确保数据是真实的。


# 练习6-3：词汇表 Python字典可用于模拟现实生活中的字典。为避免混淆，我们将后者称为词汇表。
# ❏ 想出你在前面学过的5个编程术语，将其用作词汇表中的键，并将它们的含义作为值存储在词汇表中。
# ❏ 以整洁的方式打印每个术语及其含义。
# 为此，可先打印术语，在它后面加上一个冒号，再打印其含义；
# 也可在一行打印术语，再使用换行符（\n）插入一个空行，然后在下一行以缩进的方式打印其含义。
print("\n6-3")
computers = {
    'processor':'A processor is a functional unit that interprets and carries out instructions. ',
    'Data structures':'Data structures organize data in ways that make algorithms more efficient.',
    'Wireless technologies':'Wireless technologies enable devices to communicate without physical connections'
}
for k,v in computers.items():
    print(k+":\n  "+v)

# 练习6-5：河流
# 创建一个字典，在其中存储三条重要河流及其流经的国家。
# 例如，一个键值对可能是’nile': 'egypt'。
# ❏ 使用循环为每条河流打印一条消息，下面是一个例子。The Nile runs through Egypt.
# ❏ 使用循环将该字典中每条河流的名字打印出来。
# ❏ 使用循环将该字典包含的每个国家的名字打印出来。
print("\n6-5")
rivers = {'nile':'egypt','The Yellow River':'China','The Long River':'China'}
for river,country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

# 练习6-6：调查 在6.3.1节编写的程序favorite_languages.py中执行以下操作。
# ❏ 创建一个应该会接受调查的人员名单，其中有些人已包含在字典中，而其他人未包含在字典中。
# ❏ 遍历这个人员名单。对于已参与调查的人，打印一条消息表示感谢；
#    对于还未参与调查的人，打印一条消息邀请他参加。
print("\n6-6")
persons = ['Jen','Sian','Sarah','Phil']
repo = {'Jen':'python','Sarah':'C','Edward':'Ruby','Phil':'python'}
for i in person:
    if  i in repo.keys():
        print(f"{i},thank you!")
    else:
        print(f"{i},let us finish our report.")

# 练习6-7：人们
# 在为完成练习6-1而编写的程序中，再创建两个表示人的字典，
# 然后将这三个字典都存储在一个名为people的列表中。
# 遍历这个列表，将其中每个人的所有信息都打印出来。
print("\n6-7")
person2 = {'first_name':'Steven','last_name':'Lau','age':'20','city':'Weifang'}
person3 = {'first_name':'Sean','last_name':'Lau','age':'19','city':'Shandong'}
people = [person,person2,person3]
for p in people:
    for k,v in p.items():
        print(k+':'+v)

# 练习6-8：宠物
# 创建多个表示宠物的字典，每个字典都包含宠物的类型及其主人的名字。
# 将这些字典存储在一个名为pets的列表中，再遍历该列表，并将有关每个宠物的所有信息都打印出来。
print("\n6-8")

# 练习6-9：喜欢的地方
# 创建一个名为favorite_places的字典。
# 在这个字典中，将三个人的名字用作键，并存储每个人喜欢的1～3个地方。
# 为了让这个练习更有趣些，可以让一些朋友说出他们喜欢的几个地方。
# 遍历这个字典，并将其中每个人的名字及其喜欢的地方打印出来。
print("\n6-9")
favorite_places = {
    "f1":['p1','p2'],
    "f2":['p3','p4','p5'],
    "f3":['p6','p7']
}
for k,v in favorite_places.items():
    print(k+"'s favorite places are:")
    for i in v:
        print(i,end=' ')
    print('')

# 练习6-10：喜欢的数2
# 修改为完成练习6-2而编写的程序，让每个人都可以有多个喜欢的数，
# 然后将每个人的名字及其喜欢的数打印出来。


# 练习6-11：城市
# 创建一个名为cities的字典，将三个城市名用作键。
# 对于每座城市，都创建一个字典，并在其中包含
# 该城市所属的国家、人口约数以及一个有关该城市的事实。
# 在表示每座城市的字典中，应包含country、population和fact等键。
# 将每座城市的名字以及有关信息都打印出来。