"""
try-except代码块让Python执行指定的操作，同时告诉Python发生异常时怎么办。
使用try-except代码块时，即便出现异常，程序也将继续运行：
显示你编写的友好的错误消息，而不是令用户迷惑的traceback。
"""
print("Give me 2 numbers,and I will divide them.")
print("You can enter 'q' to quit.")
while True:
    a = input("First number:")
    if a == 'q':
        break
    b = input("Second number:")
    if b == 'q':
        break
    try:
        answer = int(a)/int(b)
    except ZeroDivisionError:       # 这样出现异常就不会终止程序的运行
        print("You can't divide by 0!")
    else:
        print(answer)

"""
通过将可能引发错误的代码放在try-except代码块中，可提高程序抵御错误的能力。
依赖try代码块成功执行的代码都应放到else代码块中
"""

books = ['Alice','hhh','moby_dick']
for book in books:
    try:
        with open('10 file/10 '+book+'.txt') as Book:
            contents = Book.read()
    except FileNotFoundError:          # 如果except里写pass，就被称为静默失败
        pass
    else:
        words = contents.split()
        print(f"{book}有{len(words)}词")
