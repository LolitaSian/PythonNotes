# 练习11-1：城市和国家
# 编写一个函数，它接受两个形参：一个城市名和一个国家名。
# 这个函数返回一个格式为City, Country的字符串，如Santiago, Chile。
# 将这个函数存储在一个名为city_functions.py的模块中。
# 创建一个名为test_cities.py的程序，对刚才编写的函数进行测试（别忘了，需要导入模块unittest和要测试的函数）。
# 编写一个名为test_city_country()的方法，核实使用类似于’santiago’和’chile’这样的值来调用前述函数时，
# 得到的字符串是正确的。运行test_cities.py，确认测试test_city_country()通过了。
def city_country(city,country):
    return city.title() + ', ' + country.title()

import unittest
class TestCityCountry(unittest.TestCase):
    def test_city_country(self):
        result = city_country('beijing','china')
        self.assertEqual(result,'Beijing, China')
if __name__ == '__main__':
    unittest.main()

# 练习11-2：人口数量
# 修改前面的函数，加上第三个必不可少的形参population，并返回一个格式为
# City, Country-population xxx的字符串，如Santiago, Chile-population 5000000。
# 运行test_cities.py，确认测试test_city_country()未通过。
# 修改上述函数，将形参population设置为可选的。
# 再次运行test_cities.py，确认测试test_city_country()又通过了。
# 再编写一个名为test_city_country_population()的测试，核实可以使用类似于
# 'santiago'、'chile’和’population=5000000’这样的值来调用这个函数。
# 再次运行test_cities.py，确认测试test_city_country_population()通过了。
def city_country(city,country,population = ''):
    if population:
        result = city.title() + ', ' + country.title() + '-population ' + population
        return result
    else:
        return city.title() + ', ' + country.title()

import unittest
class TestCityCountry(unittest.TestCase):
    def test_city_country(self):
        result = city_country('beijing','china')
        self.assertEqual(result,'Beijing, China')
    def test_city_country_population(self):
        result = city_country('yantai','china','1000w')
        self.assertEqual(result,'Yantai, China-population 1000w')
if __name__ == '__main__':
    unittest.main()

# 练习11 - 3：雇员
# 编写一个名为Employee的类，其方法__init__()接受名、姓和年薪，并将它们存储在属性中。
# 编写一个名为give_raise()的方法，它默认将年薪增加5000美元，但也能够接受其他的年薪增加量。
# 为Employee编写一个测试用例，其中包含两个测试方法：
# test_give_default_raise()和test_give_custom_raise()。
# 使用方法setUp()，以免在每个测试方法中都新建雇员实例。
# 运行这个测试用例，确认两个测试都通过了。
class Employee:
    def __init__(self,first,last,salary):
        self.name = first + ' ' + last
        self.salary = salary
    def give_raise(self,num=5000):
        self.salary += num
        return self.salary

import unittest
class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee('Steven','White',5000)
    def test_give_default_raise(self):
        res = self.employee.give_raise()
        self.assertEqual(res,10000)
    def test_give_custom_raise(self):
        res = self.employee.give_raise(2000)
        self.assertEqual(res, 7000)
if __name__ == '__main__':
    unittest.main()