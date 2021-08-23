import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,6,0.1)  # 生成0-6的数据，步长为0.1
y = np.sin(x)
z = np.cos(x)

plt.plot(x, y, label="sin")
plt.plot(x, z, linestyle = "--", label="cos")

plt.xlabel("x") # x轴标签
plt.ylabel("y") # y轴标签
plt.title('sin & cos') # 标题
plt.legend() # 显示图例
plt.show() # 显示图片

from matplotlib.image import imread
img = imread('F:\Python\DeepLearning\im.jfif') # 读入图像（设定合适的路径！）
plt.imshow(img)
plt.show() # 显示图片

