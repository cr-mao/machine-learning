import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

# 生成数据
np.random.seed(1)  # 随机数种子，用于生成随机数
x = 4 + np.random.normal(0, 1.5, 200)
# np.random.normal(loc=0.0, scale=1.0, size=None)  #为一个正态分布
# loc(float)：均值，对应着这个分布的中心。loc=0说明这一个以y轴为对称轴的正态分布
# scale(float)：标准差，对应分布的宽度，scale越大越矮胖，scale越小，越瘦高
# size(int 或者整数元组)：输出的值赋在shape里，默认为None

# plot:

fig, ax = plt.subplots()

ax.hist(x, bins=8, linewidth=0.5, edgecolor="white")

ax.set(xlim=(0, 10), xticks=np.arange(1, 10),
       ylim=(0, 56), yticks=np.linspace(0, 56, 9))  # 9个，包含0，间隔为7，7×8=56，即[0,7,14,21,28,35,42,49,56]
# np.arange()：返回一个有终点和起点的固定步长的排列
# np.linspace(start, stop, num):用来创建等差数列，num为个数

plt.show()