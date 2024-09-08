import matplotlib.pyplot as plt
import random

# 数据准备
x = range(100)
y = [random.uniform(13, 20) for i in x]  # random.uniform()：随机生成13-20范围内的浮点数

plt.figure(figsize=(10, 5), dpi=80)  # 创建画布
plt.scatter(x, y, color='r', linestyle='-', label='樟树')  # 绘制折线图

x_ticks_label = ["{}天".format(i) for i in x]  # 构建x轴刻度标签
y_ticks = range(25)  # 构建y轴刻度

# 修改x,y轴坐标的刻度显示
plt.xticks(x[::10], x_ticks_label[::10])
plt.yticks(y_ticks[10:22:2])

plt.grid(True, linestyle='-', alpha=0.9)  # 添加网格
plt.legend(loc=0)  # 显示图例

# 描述信息
plt.xlabel("时间/天")
plt.ylabel("温度")
plt.title("24小时内温度变化图", fontsize=18)

plt.savefig("./scatter.jpg")  # 保存至指定位置
plt.show()  # 显示图像