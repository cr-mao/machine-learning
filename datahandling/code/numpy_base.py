"""numpy与list计算性能对比"""
import numpy as np
import time
#获取当前时间戳
t1 = time.time()
a = []
#Python列表的方式 for 循环10万次
for x in range(100000):
    #幂等计算
    a.append(x**2)
#获取当前时间戳  
t2 = time.time()
#t2减t1，求时间差
t = t2 - t1
#返回时间差
print(t)

#获取当前时间戳 
t3 = time.time()
#numpy列表方式循环10万次，并且幂等计算
b = np.arange(100000)**2
#获取当前时间戳 
t4 = time.time()
#返回t4减t3的时间差
print(t4-t3)

"""最大值"""
#生成3行3列的矩阵
a = np.arange(9).reshape(3,3)
print(a)
# 求数组的最大值
print(np.amax(a))
# 求数组行的最大值
print(np.amax(a,0))
# 求数组列的最大值
print(np.amax(a,1))

"""最小值"""
#生成3行3列的矩阵
a = np.arange(9).reshape(3,3)
print(a)
# 求数组的最小值
print(np.amin(a))
# 求数组行的最小值
print(np.amin(a,0))
# 求数组列的最小值
print(np.amin(a,1))

"""numpy.mean()的使用"""
#输入一个二行二列的矩阵
x = np.array([[1,2],[3,4]])
# 计算矩阵的均值
y = np.mean(x)
print(y)
#改变参数 axis
x = np.array([[1,2],[3,4]])
# 计算矩阵每一列的均值
print(np.mean(x, axis = 0))
# 计算矩阵每一行的均值
print(np.mean(x, axis = 1))

"""np.average()的使用"""
#输入一个二行二列的矩阵
data = np.array([[1, 2], [3, 4]])
# 计算矩阵的均值
print(np.average(data))
#改变参数 axis
# 计算矩阵每一列的均值
print(np.average(data, axis = 0))
# 计算矩阵每一行的均值
print(np.average(data, axis = 1))

print("-------------")
"""加权平均值"""
#生成3行3列的矩阵
a = np.arange(9).reshape(3,3)
print(a)
#生成一行一列的矩阵，用于加权
b= np.array([1,2,3])
#计算矩阵每一列的加权平均值
print(np.average(a,axis=0,weights=b))
#计算矩阵每一行的加权平均值
print(np.average(a,axis=1,weights=b))

"""中位数"""
#生成10行10列的矩阵
a = np.arange(100).reshape(10,10)
# 计算矩阵的中位数
print(np.percentile(a,50))
print(np.median(a))
# 计算矩阵每一列的中位数
print(np.percentile(a,50,axis=0))
print(np.median(a,axis=0))
# 计算矩阵每一行的中位数
print(np.percentile(a,50,axis=1))
print(np.median(a,axis=1))

"""分位数"""
#生成10行10列的矩阵
a = np.arange(100).reshape(10,10)
#计算矩阵的25分位数
print(np.percentile(a,25))
# 计算矩阵每一列的分位数
print(np.percentile(a,25,axis=0))
# 计算矩阵每一行的分位数
print(np.percentile(a,25,axis=1))

"""标准差"""
#生成10行10列的矩阵
a = np.arange(100).reshape(10,10)
#计算矩阵的标准差
print(np.std(a))
# 计算矩阵每一列的标准差
print(np.std(a,axis=0))
# 计算矩阵每一行的标准差
print(np.std(a,axis=1))

"""方差"""
#生成10行10列的矩阵
a = np.arange(100).reshape(10,10)
#计算矩阵的方差
print(np.var(a))
# 计算矩阵每一列的方差
print(np.var(a,axis=0))
# 计算矩阵每一行的方差
print(np.var(a,axis=1))

"""矩阵加法运算--两个矩阵相加"""
#生成两个3行3列的矩阵
a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
b = np.array([[2, 3, 4],
              [5, 6, 7],
              [8, 9, 10]])
#计算2个矩阵相加的结果
c = a+b
print(c)

"""矩阵加法运算--矩阵与标量(常数)相加"""
#生成一个3行3列的矩阵
a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
b = 3
#计算矩阵与常数3相加的结果
c = a+b
print(c)

"""矩阵减法运算--两个矩阵相减"""
#生成两个3行3列的矩阵
a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
b = np.array([[2, 3, 4],
              [5, 6, 7],
              [8, 9, 10]])
#计算2个矩阵相减的结果
c = b-a
print(c)

"""矩阵减法运算--矩阵与标量(常数)的减法运算"""
#生成一个3行3列的矩阵
a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
b = 3
#计算矩阵与常数3相减的结果
c = b-a
print(c)


print("----------------------")
"""求矩阵中每个元素的相反数"""
#生成一个3行3列的矩阵
a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
#求矩阵中每个元素的相反数
b = -a
print(b)

"""矩阵元素乘法"""
#生成两个3行3列的矩阵
a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
b = np.array([[2, 3, 4],
              [5, 6, 7],
              [8, 9, 10]])
#求两个矩阵元素乘法的结果
print(np.multiply(a, b))

"""矩阵乘法运算"""
#生成两个3行3列的矩阵, A的列数=B的行数
a = np.array([[1, 2, 3],
              [4, 5, 6]])
b = np.array([[7, 8],
              [9, 10],
              [11, 12]])
#求两个矩阵乘法的结果
print(np.dot(a, b))

"""矩阵的元素除法--也叫真除-结果既有整数部分也有小数部分"""
#生成两个2行3列的矩阵
a = np.array([[1, 2, 3],
              [4, 5, 6]])
b = np.array([[2, 6, 12],
              [20, 30, 43]])
#求两个矩阵相除的结果
print(np.divide(b,a))

"""numpy使用案例"""
#生成学生成绩
array1 = np.array([[88,90,94,90,85],[93.5,93.5,92.5,90.5,90.5],[0,0,0,0,0]])
print(array1)
#整体学生成绩修改
print( array1+0.5)
#计算学生成绩中位数
print(np.median(array1))
#计算学生成绩平均分
print(np.average(array1))
#计算学生成绩标准差
print(np.std(array1))