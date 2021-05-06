"""
 读文件
 with关键字：关键字with在不再需要访问文件后将其关闭。
 在这个程序中，注意到我们调用了open()，但没有调用close()。
 也可以调用open()和close()来打开和关闭文件，
 但这样做时，如果程序存在bug导致方法close()未执行，文件将不会关闭。
 这看似微不足道，但未妥善关闭文件可能导致数据丢失或受损。
 如果在程序中过早调用close()，你会发现需要使用文件时它已关闭（无法访问），
 这会导致更多的错误。并非在任何情况下都能轻松确定关闭文件的恰当时机，
 但通过使用前面所示的结构，可让Python去确定：你只管打开文件，
 并在需要时使用它，Python自会在合适的时候自动将其关闭。
"""
# 读取整个文件
with open('10 file/10 test_file.txt') as Poem:
    contents = Poem.read()
print(contents)

# 按行读取
with open('10 file/10 test_file.txt') as Poem:
    for line in Poem:
        print(line.rstrip())    # 加上rstrip消除空行
# 建一个包含文件各行内容的列表
with open('10 file/10 test_file.txt') as Poem:
    lines = Poem.readlines()    # 返回一个每行文字的列表
for line in lines:
    print(line.rstrip())

pi = ''
with open("10 file/10 pi.txt") as Pi:
    for line in Pi:
        pi += line.strip()      # strip消除空格
print(f"{pi[0:32]}")    # π后100w位，打印前30位

birth = input("请输入你的生日，例如0315：")
if birth in pi:
    print("π中有你的生日！")
else:
    print("π中没你的生日！")

"""
如果要写入的文件不存在，函数open()将自动创建它。然而，以写入模式（'w'）打开文件时千万要小心，
因为如果指定的文件已经存在，Python将在返回文件对象前清空该文件的内容。
"""
with open('10 file/10 write_demo.txt','w') as Demo:
    Demo.write("I love Python!!!")
with open('10 file/10 write_demo.txt','a') as Demo:
    Demo.write("\nI love Python!")


'''
JSON
'''
import json
try:
    with open('10 file/10 JSON.json') as File:
        contents = json.load(File)
except FileNotFoundError:
    with open('10 file/10 JSON.json', 'w') as File:
        name = input("请输入名字：")
        print(f"hello {name}")
        json.dump(name, File)
else:
    print(f"hello {contents},welcome back.")
