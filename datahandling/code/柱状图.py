import matplotlib.pyplot as plt
import random

from pylab import mpl
mpl.rcParams["font.sans-serif"] = ["SimHei"]  # 设置显示中文字体
mpl.rcParams["axes.unicode_minus"] = False  # 设置正常显示符号

# 数据准备
x = range(0, 10)
y = [random.randint(35, 45) for i in x]  # random.uniform()：随机生成13-20范围内的浮点数

plt.figure(figsize=(10, 5), dpi=80)  # 创建画布
plt.bar(x, y, width=0.5, color=['b', 'r', 'g', 'y', 'c', 'm', 'y', 'k', 'c', 'g'])  # 绘制折线图

x_ticks_label = ["21{}班".format(i) for i in x]  # 构建x轴刻度标签
y_ticks = range(55)  # 构建y轴刻度

# 修改x,y轴坐标的刻度显示
plt.xticks(x[::1], x_ticks_label[::1])
plt.yticks(y_ticks[0:55:5])

plt.grid(True, linestyle=':', alpha=0.3)  # 添加网格

# 描述信息
plt.xlabel("班级")
plt.ylabel("人数")
plt.title("2021级各班人数柱状图", fontsize=18)

plt.savefig("./bar.jpg")  # 保存至指定位置
plt.show()  # 显示图像