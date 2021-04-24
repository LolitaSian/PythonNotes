print('hello')

# 井号开头单行注释
'''
三个单引号多行注释
'''
"""
三个双引号多行注释
"""

# 定义变量 名 = 值
# 定义常量 常量名全大写字母，其值在整个生命周期保持不变
name = 'Sian'

# 数据类型
# - Number
#     - int
#     - long Python2中的长整型，Python3中都用int
#     - float
#     - complex 复数
# - String
# - Bool
# - List
# - Tuple 元组
# - Dictionary 字典
#
#                                                                                                                                                                     python中不用开发者声明数据类型，系统会自动辨别
# 可以使用type来查看变量类型


# 标识符，变量名 Python中标识符区分大小写
import keyword
# 导包 查看系统关键字
print(keyword.kwlist)

print('1+2=',3)

age = 24
# 格式化输出 占位符%s %f %d0
print("我是%s，我%d岁" %(name,age))
print("%.2f" %3.1415)
print('%%',"hello %s %%" %name)
# 使用格式化输出的时候，想输出%需要打两个

# python 3.6之后支持f-string，使用{}占位任何数据类型
# 变量写在{}中间,输出的整个字符之前加上f
print(f"my name is {name}")
# Python3.6之前可以还可以用format()
print("my name is {}".format(name))


myName = 'sian lAu '
print(myName)
print(myName.lower())   # 字符串转换为小写
print(myName.title())   # 字符串转换为首字母大写
print(myName.upper())   # 字符串转换为大写
print(myName.rstrip())  # 去掉末尾的空格，不会改变原字符串
# lstrip()开头空格 strip()两边空格


# print默认结尾是\n，但是可以修改
print('hello',end='__')
print('world')

# input('给用户的提示信息') 获取用户输入，遇到回车停止，得到的数据都是字符串类型
password = input('请输入密码：')
print("你的密码是%s" %password)

# 强制类型转换
f = 3.14
num = int(f)
s = 'h'
print(type(num))
print(type(eval('f')))
print(type(eval('num')))
print(type(eval('5.1')))
#　eval还原字符串的数据类型
# - 如果字符串内是数字直接还原数据类型
# - 如果字符串内是字符，会寻找是否有该名称变量
#   - 如果有则输出变量类型
#   - 如果没有则报错
#   - 比如：print(type(eval('num'))) 输出int print(type(eval('num1'))) 报错


# 算术运算符
print(1+3)
print(1-3)
print(1*3)
print(1/3)
print(1%3)
print(1//3)     # 取整除
print(3**2)     # 求幂

# 赋值运算符
str1 = 'asd'
str2,str3 = 'da','dsa'
print(str1,str2,str3)

# 逻辑运算符 and or not
flag = False
print(not flag)