import numpy as np
# 要生成NumPy数组，需要使用np.array()方法。np.array()接收
# Python列表作为参数，生成NumPy数组（numpy.ndarray）

l1 = [1.0,2.0,3.0]
l2 = [4.0,5.0,6.0]

x = np.array(l1)          # arr1创建数组x，注意区别数组没有逗号分割
print('x = ',x)
print('type of x:',type(x))
print('a = ',l1)
print('type of a:',type(l1))

y = np.array(l2)

# 数组的操作都是对每个元素进行的
print(f"x = {x} \ny = {y}")
print('x+y:\n',x+y)
print('x-y:\n',x-y)
print('x*y:\n',x*y)
print('x/y:\n',x/y)
print('x+2:\n',x+2)
print('x-2:\n',x*2)

print('_____________________________')

# NumPy不仅可以生成一维数组（排成一列的数组），也可以生成多维数组。
# 比如，可以生成如下的二维数组（矩阵）

matrix = [[1,2,3],[4,5,6],[7,8,9]]

m = np.array(matrix)
print(m)

print('shape:',m.shape) # 矩阵A的形状
print('ndim:',m.ndim) # 维度
print('dtype:',m.dtype) # 矩阵元素的数据类型可以通过dtype查看
# 如果不指定数据类型，那python会自动分析确定数据类型，也可以自己指定
n = np.array(matrix,dtype='float64')
print('dtype:',n.dtype) # 矩阵元素的数据类型可以通过dtype查看


# 同形矩阵可以进行算术运算，矩阵可以和数字运算
# 矩阵也可以和numpy的数组运算，前提是列数相同，这一功能为广播broadcast
print('_____________________________')


# 其他声明方法:
# 一个参数
a = np.arange(5)    # 取值范围[0,5)
print('a = np.arange(5):',a)
# 两个参数
b = np.arange(2,8)      # 取值范围[2,8)
print('b = np.arange(2,8):',b)
# 三个参数
c = np.arange(1,4,0.5)      # 取值范围[1,4)
print('c = np.arage(1,4,0.5):',c)

# np.random中的函数可以创建随机一维数组

# 想生成高维的在括号里用逗号分隔
print('\nnp.random')
print(np.random.rand(5,2))
print(np.random.randn(2,3))   # 产生的随机数服从标准正态分布（均值为0、标准差为1的分布）
print(np.random.randint(1,13,(2,3)))  # 随机整数

# zeros可以一次性创造全0数组，ones可以一次性创造全1数组。empty则可以创建一个没有初始化数值的数组。
# 想要创建高维数组，则需要为shape传递一个元组
print('np.zeros((2,5)):\n',np.zeros((2,5)))
print('np.ones((2,3)):\n',np.ones((2,3)))
print('np.empty((2,3)):\n',np.empty((2,3)))

print('_____________________________')

# reshape
print(np.random.randn(4).reshape(2,2))
print(np.random.randn(2,2))
print(np.arange(12).reshape(4,3))

# 索引访问元素

print('m = \n',m)
print('m[0] = ',m[0])
print('m[0,2] = ',m[0,2])

# for
for row in m:
    print(row)

# flatten()扁平化将其显示为一维数组
print(m.flatten())
m=m.flatten()

# 获取m中索引为0 2 4的元素
print(m[np.array([0, 2, 4])])

# 条件语句
print(m>5)

print(m[m>5])