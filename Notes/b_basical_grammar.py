# if 条件语句:
#     条件成立，执行语句
age = input("请输入年龄：")   #input接受结果字符串
age = int(age)
if age > 18:
    print(f"哥{age}岁了")
    print("哥可以去网吧了")
else:
    print("未成年禁止")


if age<20:
    print("少年")
elif age<30 and age >=20:
    print("中年")
elif age>=30 and age <50:
    print("中年")
else:
    print("老年")

# 三目运算 变量 = 表达式1 if 判断条件 else 表达式2    扁平化
a = int(input("请输入a："))
b = int(input("请输入b："))
print(a-b if a>b else b-a)

# while 条件语句:
#     条件满足，执行语句

while age < 20 and age > 0:
    print(age,end=' ')
    age-=1
print('\n')

# for 临时变量 in 列表或字符串等可迭代对象:
#     满足条件，执行语句
str = 'hello Sian'
for i in str:
    print(i,end = '_')
print('\n')

for i in str:
    if i == 'a':
        break
    print(i,end = '')
print('\n')

for i in str:
    if i == 'a':
        continue
    print(i,end = '')
print('\n')

# 局部作用域和全局作用域
variable = 'global'     # 全局变量
def function1():
    print("function1 "+variable)     # 函数中无声明 访问全局变量
def function2():
    variable = 'local'  # 函数中有声明 访问局部变量
    print("function2 "+variable)
print(variable)
function1()
function2()
def modify1():
    global variable     # 函数中可用global指明全局变量，对其进行修改
    variable = 'modify1_global'
def modify2():
    variable = 'modify2_global'     # 可以访问全局变量，不使用global不能修改
modify1()
print(variable)
modify2()
print(variable)