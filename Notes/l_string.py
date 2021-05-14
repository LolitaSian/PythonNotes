print("Sian's demo.")
print('Sian\'s demo.')      # \ 转义字符
print(r'Sian\'s demo.')     # r 原始字符
print('''Sian's             
demo.''')                   # 三引号可以打印原始格式的制表符、换行符、引号

string = "Sian is learing Python."
print("\nstring:",string)
print("string[5]:",string[5])
print('string[5:-5]:',string[5:-5])
print('"L" in string:','L' in string)   # in / not in
print('"l" in string:','l' in string)

# upper() lower() title()
print("\nupper() lower() title()")
print(string.upper())
print(string.lower())
print(string.title())

# startwith() endwith()
print("\nstartwith() endwith()")
print('string.startswith("Si"):',string.startswith("Si"))
print('string.startswith("si"):',string.startswith("si"))
print('string.endswith("hon."):',string.endswith("hon."))
print('string.endswith("thon"):',string.endswith("thon"))

# join() split()
print("\njoin() split()")
lis1 = string.split('i')
lis2 = string.split(' ')
print("string.split('i'):",lis1)
print("string.split(' '):",lis2)
str1 = "❤".join(lis1)
str2 = "△".join(lis2)
print('"❤".join(lis1):',str1)
print('"△".join(lis2):',str2)

# isX()
print("\nisX()")
print('HELLO.islower():','HELLO'.islower())
print('HEllo.isupper():','HEllo'.isupper())
print('Hello.istitle():','Hello'.istitle())
print("'hello123'.isalpha():",'hello123'.isalpha())     # 是否只有字母且不为空
print("'hello123'.isalnum():",'hello123'.isalnum())     # 是否只有字母和数字且不为空
print("'hello123'.isdecimal():",'hello123'.isdecimal()) # 是否只有数字且不为空
print("'   '.isspace():",'    '.isspace())          # 是否只有空格且不为空

# ljust() rjust() center(a,b) 填充文本
# 第一个参数占位大小；第二个参数填充字符，默认是空格
print("\nljust() rjust() center() 填充文本")
print("'hello'.rjust(20):",'hello'.rjust(20))
print("'hello'.ljust(20):",'hello'.ljust(20))
print("'hello'.center(20):",'hello'.center(20))
print("'hello'.rjust(20,'*'):",'hello'.rjust(20,'*'))
print("'hello'.ljust(20,'-'):",'hello'.ljust(20,'-'))
print("'hello'.center(20,'_'):",'hello'.center(20,'_'))

# strip
print("\nstrip去空格")
string2 = "   hello world.    "
print("string2:",string2)
print("string2.rstrip():",string2.rstrip())
print("string2.lstrip():",string2.lstrip())
print("string2.strip():",string2.strip())

# pyperclip  copy() paste()可以向计算机剪贴板发送接受文本
print("\npyperclip")
import pyperclip
pyperclip.copy("hel0000")       # 修改剪贴板
str = pyperclip.paste()         # 返回剪贴板内容
print(str)

