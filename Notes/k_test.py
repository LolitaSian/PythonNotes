"""
测试函数
"""
def show_name(first,last):
    name = first + " " + last
    return name.title()

print("you can enter 'q' to quit")
while True:
    first = input("first name:")
    if first == 'q':
        break
    last = input("last name:")
    if last == 'q':
        break
    print(show_name(first,last))


# 先导入模块unittest和要测试的函数，再创建一个继承unittest.TestCase的类
import unittest
class NameTest(unittest.TestCase):
    # 方法名必须以test_打头
    def test_show_name(self):       # 只包含一个方法，用于测试函数的一个方面
        result = show_name('sian','lau')
        self.assertEqual(result,'Sian Lau') # 断言方法:核实得到的结果是否与期望的结果一致

# 检查特殊变量__name__，这个变量是在程序执行时设置的。如果这个文件作为主程序执行，
# 变量__name__将被设置为’__main__'。在这里，调用unittest.main()来运行测试用例。
# 如果这个文件被测试框架导入，变量__name__的值将不是’__main__'，因此不会调用unittest.main()。
if __name__ == '__main__':
    unittest.main()


# 测试未通过时，不要修改测试，而应修复导致测试不能通过的代码：
# 检查刚刚对函数所做的修改，找出导致函数行为不符合预期的修改。

"""
6个常用的断言方法，只能在继承unittest.TestCase的类中使用这些方法
self.assertEqual(a,b)       a,b相同
self.assertNotEqual(a,b)    a,b不同
self.assertTrue(a)          a为True
self.assertFalse(a)         a为False
self.assertIn(i,list)       i在list中
self.assertNotIn(i,dic)     i不在dictionary中
"""

"""
测试类
"""
class Quiz:
    def __init__(self,question):
        self.question = question
        self.result = {}
    def show_question(self):
        print(self.question)
    def store_result(self,res):
        if res in self.result.keys():
            self.result[res] += 1
        else:
            self.result[res] = 1
    def show_result(self):
        for k,v in self.result.items():
            print(f"○ {k}:{v}")
quiz = Quiz("\n\nwhich programming language do you like?")
quiz.show_question()
print("you can enter 'q' to quit")
while True:
    name = input("please input your respond:")
    if name =='q':
        break
    quiz.store_result(name)
print("Survey Result:")
quiz.show_result()
'''
class TestQuiz(unittest.TestCase):
    def test_quiz(self):    # 测试单个样例
        quiz = Quiz("\nwhich programming language do you like?")
        quiz.store_result('python')
        self.assertIn('python',quiz.result)
    def test_quiz_many_result(self):
        my_quiz = Quiz("\nwhich programming language do you like?")
        result = ['C++','Java','Python','C++','JavaScript']
        for i in result:
            my_quiz.store_result(i)
        for i in result:
            self.assertIn(i,my_quiz.result)

if __name__ == '__main__':
    unittest.main()
'''
# setUp()让我们只需创建这些对象一次，就能在每个测试方法中使用。
class TestQuiz2(unittest.TestCase):
    def setUp(self):
        self.quiz = Quiz("\nwhich programming language do you like?")
        self.result = ['C++','Java','Python','C++','JavaScript']
    def test_quiz(self):    # 测试单个样例
        self.quiz.store_result(self.result[0])
        self.assertIn(self.result[0],self.quiz.result)
    def test_quiz_many_result(self):
        for i in self.result:
            self.quiz.store_result(i)
        for i in self.result:
            self.assertIn(i,self.result)
if __name__ == '__main__':
    unittest.main()