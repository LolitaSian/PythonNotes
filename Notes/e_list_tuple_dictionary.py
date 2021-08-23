# 列表
print("列表")
my_list = [1,2,3,4,5]
print("my_list:",my_list)
print('my_list[0]:',my_list[0])           # 用下标获取元素
print("my_list[-2]:",my_list[-2])         # 负数下标
print("my_list[1:4]:",my_list[1:4])       # 切片
print('my_list+my_list:',my_list+my_list) # 相加
print('2*my_list:',2*my_list)             # 相乘
print('len(my_list):',len(my_list),'\n')       # len()获取长度

del my_list[1]                         # del用下标删除
print("del my_list[1] :",my_list)
my_list.remove(4)                      # .remove()用值删除
print("my_list.remove(4):",my_list)

print("5 in my_list:",5 in my_list)     # in / not in 逻辑
print('4 in my_list:',4 in my_list)
print('4 not in my_list:',4 not in my_list)

my_list.append(6)                           # 添加元素
print("my_list.append(6):",my_list)
my_list.insert(1,7)                         # 插入元素
print("my_list.insert(1,7):",my_list)
print('my_list.index(5):',my_list.index(5)) # 在就返回位置，不在就ValueError
my_list.sort()                              # 排序
print("my_list.sort():",my_list)
print('my_list.count(7):',my_list.count(7)) # 某一元素出现次数

print('\n随机' )
import random
messages = [
    'It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']
print(messages[random.randint(0, len(messages) - 1)])
print(random.choice(messages))

print("\n\n元组")
# 元组与列表的区别就是用圆括号，只有一个元素的时候后边也要接一个逗号
# 元组数据不能修改，但是可以重新赋值
my_tuple = (1,2,3,4,5)
print(my_tuple)
my_tuple = (6,7,8,9,0)
print(my_tuple)
print('my_tuple.index(7):',my_tuple.index(7))

print("\nmy_list()和my_tuple()")
# my_list()和my_tuple()可以进行类型转换
print('list("hello"):',list('hello'))
print("tuple('world'):",tuple('world'))
print('list((1,2,3)):',list((1,2,3)))
print("tuple([1,2,3]):",tuple([1,2,3]))


# 字典
print("\n字典")
# 字典是不排序的，但是python3.x以后输出是有序的
eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
print(eggs == ham)

dic1 = {'Sian':'07.10','Hick':'07.10','Lily':'11.01','Steven':'11.16'}

# 添加元素
dic1['Sean'] = '05.07'

# 遍历
print("\nkeys(),values(),items()")
for i in dic1.keys():
    print("keys:",i)
for i in dic1.values():
    print("values:",i)
for i in dic1.items():
    print("items:",i)
for k,v in dic1.items():
    print("key:"+k , "value:"+v)

print("'Sean' in dic1:",'Sean' in dic1)
print("'Sian' in dic1.keys():",'Sian' in dic1.keys())
print("'Sian' not in dic1.keys():",'Sian' not in dic1.keys())
print("'Sian' not in dic1.values():",'Sian' not in dic1.values())

# get(a,b) a是要取得的键值，b是如果a不存在则返回b
print("dic1.get('Sian','06.06'):",dic1.get('Sian','06.06'))
print("dic1.get('Siann','06.06'):",dic1.get('Siann','06.06'))

# setdefault(a,b) 如果a存在就返回a的值；如果a不存在就返回b，并把b赋值给a
print("\nsetdefault(a,b)")
print("dic1.setdefault('Sian','0606'):",dic1.setdefault('Sian','0606'))
print("dic1.setdefault('Siann','06.06'):",dic1.setdefault('Siann','06.06'))
print("dic1.setdefault('Siann','07.07'):",dic1.setdefault('Siann','07.07'))

# pprint()和pformat()
print("\npprint")
import pprint
messages = "My first demo is Hello World."
dic2 = {}
print(messages,'\ndic2=')
for character in messages:          # 统计字符出现频率
    dic2.setdefault(character,0)
    dic2[character] += 1
pprint.pprint(dic2)                 # = print(pprint.pformat(dic2))
# pprint.pformat(dic2) 把字典转换为完美形式的字符串


print("\n\n引用，深拷贝浅拷贝")
lis1 = [1,2,3]
lis2 = lis1
lis2[0] = 3
tup1 = (1,2,3)
tup2 = tup1
tup2 = (4,5,6)
dic1 = {0:1,1:2,2:3}
dic2 = dic1
dic2[0] = 7
str4 = 'hello'
str5 = str4
str5 = 'world'
a,b,c,g = 1,1.5,'2',False
d,e,f,h = a,b,c,g
d,e,f,h = 3,3.5,'4',True
print(lis1,lis2)        # 列表和字典涉及到深拷贝浅拷贝的问题
print(dic1,dic2)
print(tup1,tup2)
print(str4,str5)
print(a,b,c,g,d,e,f,h)

lis3 = [7,8,9,'10',[4,5,6]]
import copy
lis4 = copy.copy(lis3)          # 不完全的深拷贝，只能拷贝一层
lis4[-1][1] = 666
lis5 = copy.deepcopy(lis3)      # 可以实现多层嵌套深拷贝
lis5[-1][1] = 777
print(lis3)
print(lis4)
print(lis5)