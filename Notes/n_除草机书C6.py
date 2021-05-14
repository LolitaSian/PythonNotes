"""
项目：口令保管箱
复制账户名称。然后查询保管箱内是否有对应密码，如果有就返回到剪贴板中。
"""
PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}
import pyperclip

account = pyperclip.paste()     # 获取账户
if account in PASSWORDS:        # 查看账户是否被存储
    pyperclip.copy(PASSWORDS[account])      # 如果被存储就返回给剪贴板
    print('Password for ' + account + ' copied to clipboard.')
else:                                       # 没存储
    print('There is no account named ' + account)
    # 随手增加一个新功能，添加不存在的密码
    password = input(f"Do you want to save the password of {account}? "    
                     "\nEnter your password to save"
                     "\nor press 'Enter' to quit:")
    if password:
        PASSWORDS[account] = password
print(PASSWORDS)

'''
项目：在 Wiki 标记中添加无序列表
在编辑一篇维基百科的文章时，你可以创建一个无序列表，即让每个列表项占据一行，并在前面放置一个星号。
但是假设你有一个非常大的列表，希望添加前面的星号。你可以在每一行开始处输入这些星号，一行接一行。
或者也可以用一小段Python 脚本，将这个任务自动化。
bulletPointAdder.py 脚本将从剪贴板中取得文本，在每一行开始处加上星号和空格，
然后将这段新的文本贴回到剪贴板。
例如，如果我将下面的文本复制到剪贴板
（取自于维基百科的文章“List of Lists of Lists”）：
        Lists of animals
        Lists of aquarium life
        Lists of biologists by author abbreviation
        Lists of cultivars
然后运行 bulletPointAdder.py 程序，剪贴板中就会包含下面的内容：
        * Lists of animals
        * Lists of aquarium life
        * Lists of biologists by author abbreviation
        * Lists of cultivars
这段前面加了星号的文本，就可以粘贴回维基百科的文章中，成为一个无序列表。
'''
import pyperclip
def bulletPointAdder(s):
    arr = s.split("\n")
    for i in range(0,len(arr)):
        arr[i] = '○ '+ arr[i]
    return "\n".join(arr)
str1 = """Lists of animals
Lists of aquarium life
Lists of biologists by author abbreviation
Lists of cultivars"""
pyperclip.copy(str1)            # 向剪贴板传递内容
str2 = pyperclip.paste()        # 获取剪贴板文字
res = bulletPointAdder(str2)    # 修改剪贴板内容
pyperclip.copy(res)             # 向剪贴板发送修改后内容
print(pyperclip.paste())        # 打印剪贴板处理结果


