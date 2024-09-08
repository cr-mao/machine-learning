import matplotlib.pyplot as plt
import random

from pylab import mpl

mpl.rcParams["font.sans-serif"] = ["SimHei"]  # 设置显示中文字体
mpl.rcParams["axes.unicode_minus"] = False  # 设置正常显示符号

# 数据准备
x = range(24)
y = [random.uniform(13, 20) for i in x]  # random.uniform()：随机生成13-20范围内的浮点数

plt.figure(figsize=(10, 5), dpi=80)  # 创建画布
plt.plot(x, y, color='y', linestyle='-', label='温度')  # 绘制折线图

x_ticks_label = ["{}:00".format(i) for i in x]  # 构建x轴刻度标签
y_ticks = range(40)  # 构建y轴刻度

# 修改x,y轴坐标的刻度显示
plt.xticks(x[::2], x_ticks_label[::2])
plt.yticks(y_ticks[10:20:1])

plt.grid(True, linestyle='-', alpha=0.9)  # 添加网格
plt.legend(loc=0)  # 显示图例

# 描述信息
plt.xlabel("时间")
plt.ylabel("温度")
plt.title("24小时内温度变化图", fontsize=18)

plt.savefig("./plot.jpg")  # 保存至指定位置
plt.show()  # 显示图像