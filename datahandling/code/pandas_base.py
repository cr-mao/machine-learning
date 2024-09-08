import pandas as pd
import numpy as np
from numpy import nan as NA

"""创建一个空Series"""
# 使用pd.Series()创建内容为空的一维数组对象
s = pd.Series() 
# 打印结果
print(s) 

"""通过索引访问Series数据"""
#使用pd.Series创建内容为[1,2,3,4,5]的一维数组，并指定索引为:['a','b','c','d','e']
s = pd.Series([1,2,3,4,5],index=['a','b','c','d','e']) 
# 打印索引为a的数据
print(s['a'])

"""从字典创建一个Series"""
#定义一个字典
data = {'a':0., 'b':1., 'c':2.} 
# 利用pd.Series格式化字典，变成一个一维数组
s = pd.Series(data) 
# 打印结果
print(s) 

"""检索Series中的前三个元素"""
# 使用pd.Series创建内容为[1,2,3,4,5]的一维数组，并指定索引为:['a','b','c','d','e']
s = pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
# 打印一维数组中的前三个数据
print(s[0:3])

"""通过索引访问Series数据"""
#使用pd.Series创建内容为[1,2,3,4,5]的一维数组，并指定索引为:['a','b','c','d','e']
s = pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
print(s['a'])# 打印索引为a的数据

"""使用索引获取多个元素"""
#使用pd.Series创建内容为[1,2,3,4,5]的一维数组，并指定索引为:['a','b','c','d','e']
s = pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
# 打印索引为a','b','c'的多个数据
print(s[['a','b','c']]) 

"""axes示例"""
# 使用np.random.randn随机生成4个数，并使用pd.Series生成一个一维数组
s = pd.Series(np.random.randn(4))
print('The axes are:')
#打印索引信息
print(s.axes) 

"""empty示例"""
# 使用np.random.randn随机生成4个数，并使用pd.Series生成一个一维数组
s = pd.Series(np.random.randn(4)) 
print('Is the object empty?')
#判断一维数组对象是否为空，如果为空，返回True
print(s.empty) 

"""ndim示例"""
# 使用np.random.randn随机生成4个数，并使用pd.Series生成一个一维数组
s = pd.Series(np.random.randn(4))
#返回一维数组的维度，默认定义:1
print(s.ndim) 

"""size示例"""
# 使用np.random.randn随机生成4个数，并使用pd.Series生成一个一维数组
s = pd.Series(np.random.randn(2))
# 返回基一维数组的元素个数
print(s.size) 

"""values示例"""
# 使用np.random.randn随机生成4个数，并使用pd.Series生成一个一维数组
s = pd.Series(np.random.randn(4)) 
# 将Series作为ndarray返回
print(s.values) 

"""head和tail示例"""
# 使用np.random.randn随机生成4个数，并使用pd.Series生成一个一维数组
s = pd.Series(np.random.randn(4))
# 返回数组的前2行
print(s.head(2)) 
# 返回数组的最后2行
print(s.tail(2)) 

"""创建一个空的DataFrame"""
#创建一个空的二维数组
df = pd.DataFrame() 
#返回空的二维数组
print(df) 

"""二维列表创建dataFrame并指定dtype"""
#创建二维数组
data = [['Alex',10],['Bob',12],['Clarke',13]] 
#使用DataFrame格式化，并指定列标签为['Name','Age']，每列数据类型为float
df = pd.DataFrame(data,columns=['Name','Age'],dtype=float)
#返回二维列表
print(df)

"""从ndarrays/Lists的字典来创建DataFrame"""
#创建一个字典，字典中的值为列表
data = {'Name':['Tom','Jack','Steve','Ricky'],'Age':[28,34,29,42]}
#使用DataFrame格式化
df = pd.DataFrame(data)
#返回二维列表
print(df)

"""从字典的列表创建DataFrame"""
#创建一个列表，列表中包含2个字典
data = [{'a':1,'b':2},{'a':5,'b':10,'c':20}]
#使用DataFrame格式化
df = pd.DataFrame(data)
#返回二维列表
print(df)

"""从Series字典来创建DataFrame"""
#创建一个字典，字典的每个值都是通过pd.Series格式化为一维数组并指定index
d = {'one':pd.Series([1,2,3],index=['a','b','c']),'two':pd.Series([1,2,3,4],index=['a','b','c','d'])}
#使用DataFrame格式化
df = pd.DataFrame(d)
#返回二维列表
print(df)

"""sum()示例"""
#创建一个字典，字典的每个值都是通过pd.Series格式化为一维数组
d = {'name':pd.Series(['tom','james','ricky','vin','steve','minsu','jack','lee','david','gasper','betina','andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}
#使用DataFrame格式化
df = pd.DataFrame(d)
#根据二维数组的列求和
print(df.sum(axis=1)) 

"""mean()示例"""
import pandas as pd
#创建一个字典，字典的每个值都是通过pd.Series格式化为一维数组
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}
#使用DataFrame格式化
df = pd.DataFrame(d)
#返回二维数组列的平均数
print(df.mean()) 

"""std()示例"""
import pandas as pd
#创建一个字典，字典的每个值都是通过pd.Series格式化为一维数组
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}
df = pd.DataFrame(d)#使用DataFrame格式化
print(df.std())#返回列的标准偏差

"""describe()示例"""
import pandas as pd
import numpy as np
#创建一个字典，字典的每个值都是通过pd.Series格式化为一维数组
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}
#使用DataFrame格式化
df = pd.DataFrame(d)
#返回列的统计信息的摘要
print(df.describe())
print('#################')
#返回汇总字符串列结果
print(df.describe(include=['object']))

"""agg()示例"""
# 使用pd.DataFrame格式化二维数组，并指定列标签
df = pd.DataFrame([[9,4,6,9],[8,10,7,6],[7,6,8,5]],columns=['maths','english','science','history'])
# 返回二维数组中每一列的总和、最小和最大
print(df.agg(['sum','min','max']))

"""groupby()示例"""
# 使用pd.DataFrame格式化二维数组，并指定列标签
df = pd.DataFrame([[9,4,6,9],[8,10,7,6],[7,6,8,5]],columns=['maths','english','science','history'])
# 使用groupby()函数将数据按 “Maths “值分组
a = df.groupby('maths')
# 返回按 “Maths “值分组的结果
print(a.first())

"""merge 拼接方式---内连接"""
# 通过pd.DataFrame生成两个二维数组
df1 = pd.DataFrame({'alpha':['A','B','B','C','D','E'],'feature1':[1,1,2,3,3,1],
                    'feature2':['low','medium','medium','high','low','high']})
df2 = pd.DataFrame({'alpha':['A','B','B','F'],'pazham':['apple','orange','pine','pear'],
                    'kilo':['high','low','high','medium'],'price':np.array([5,6,5,7])})
# 返回两个二维数组的内容
print(df1)
print(df2)
# 两个二维数组进行内连接,连接键的字段为：alpha
df3 = pd.merge(df1,df2,how='inner',on='alpha')

"""merge 拼接方式---外连接"""
# 通过pd.DataFrame生成两个二维数组
df1 = pd.DataFrame({'alpha':['A','B','B','C','D','E'],'feature1':[1,1,2,3,3,1],
                    'feature2':['low','medium','medium','high','low','high']})
df2 = pd.DataFrame({'alpha':['A','B','B','F'],'pazham':['apple','orange','pine','pear'],
                    'kilo':['high','low','high','medium'],'price':np.array([5,6,5,7])})
# 返回两个二维数组的内容
print(df1)
print(df2)
# 两个二维数组进行外连接,连接键的字段为：alpha
df3 = pd.merge(df1,df2,how='outer',on='alpha')

"""merge 拼接方式---左连接"""
# 通过pd.DataFrame生成两个二维数组
df1 = pd.DataFrame({'alpha':['A','B','B','C','D','E'],'feature1':[1,1,2,3,3,1],
                    'feature2':['low','medium','medium','high','low','high']})
df2 = pd.DataFrame({'alpha':['A','B','B','F'],'pazham':['apple','orange','pine','pear'],
                    'kilo':['high','low','high','medium'],'price':np.array([5,6,5,7])})
# 返回两个二维数组的内容
print(df1)
print(df2)
# 两个二维数组进行左连接,连接键的字段为：alpha
df3 = pd.merge(df1,df2,how='left',on='alpha')

"""merge 拼接方式---右连接"""
# 通过pd.DataFrame生成两个二维数组
df1 = pd.DataFrame({'alpha':['A','B','B','C','D','E'],'feature1':[1,1,2,3,3,1],
                    'feature2':['low','medium','medium','high','low','high']})
df2 = pd.DataFrame({'alpha':['A','B','B','F'],'pazham':['apple','orange','pine','pear'],
                    'kilo':['high','low','high','medium'],'price':np.array([5,6,5,7])})
# 返回两个二维数组的内容
print(df1)
print(df2)
# 两个二维数组进行右连接,连接键的字段为：alpha
df3 = pd.merge(df1,df2,how='right',on='alpha')

"""concat方法---行拼接"""
# 使用pd.Series生成2个一维数组，并指定索引
df1 = pd.Series([1.1,2.2,3.3],index=['i1','i2','i3'])
df2 = pd.Series([4.4,5.5,6.6],index=['i2','i3','i4'])
# 返回两个一维数组的内容
print(df1)
print(df2)
# 返回行拼接df1和df2的结果
print(pd.concat([df1,df2]))

"""遍历-for 循环遍历"""
# 定义一个字典
data = {"name":['Alice','Bob','Charlie'],
        "age":[25,30,35],
        "gender":['F','M','M']}
# 使用pd.DataFrame格式化
df = pd.DataFrame(data)
# 通过for循环获取二维数组中的每一行数据
for index,row in df.iterrows():
    print(f"Index:{index},Row:{row['name']},{row['age']},{row['gender']}")

# 通过for循环获取二维数组中的每一列数据
for column,value in df.iteritems():
    print(f"Column:{column}")
    print(value)

"""遍历-apply() 方法"""
# 定义一个字典
data = {"name":['Alice','Bob','Charlie'],
        "age":[25,30,35],
        "gender":['F','M','M']}
# 使用pd.DataFrame格式化
df = pd.DataFrame(data)
# 定义一个函数，实现传入的x值自动加1
def add_one(x):
    return x+'1'
# 使用apply调用add_one函数（作用于DataFrame中的每个行或者列），生成一个新的二维数组
df_new = df.apply(add_one)
# 返回新的二维数组
print(df_new)

"""遍历-applymap() 方法"""
# 定义一个字典
data = {"name":['Alice','Bob','Charlie'],
        "age":[25,30,35],
        "gender":['F','M','M']}
# 使用pd.DataFrame格式化
df = pd.DataFrame(data)
# 定义一个函数，实现传入的x值自动加1
def add_one(x):
    return x+'1'
# 使用applymap调用add_one函数（做用于DataFrame中的所有元素），生成一个新的二维数组
df_new = df.applymap(add_one)
# 返回新的二维数组
print(df_new)

"""遍历-map()方法"""
# 使用pd.Series生成新的一维数组
s = pd.Series([1,2,3])
# 定义一个函数，实现传入的x值自动加1
def add_one(x):
    return x+1
# 使用map调用add_one函数（做用于Series中的所有元素），生成一个新的一维数组
s_new = s.map(add_one)
print(s_new)

"""遍历-itteritems()方法"""
# 定义一个字典
data = {"name":['Alice','Bob','Charlie'],
        "age":[25,30,35],
        "gender":['F','M','M']}
# 使用pd.DataFrame格式化
df = pd.DataFrame(data)
# 通过for循环获取二维数组中的每一列数据
for col_label,column in df.iteritems():
    # 返回循环的数据
    print(col_label)
    print(column)

"""遍历-itertuples()方法"""
# 定义一个字典
data = {"name":['Alice','Bob','Charlie'],
        "age":[25,30,35],
        "gender":['F','M','M']}
# 使用pd.DataFrame格式化
df = pd.DataFrame(data)
# 命名元组的形式遍历 DataFrame 的行
for row in df.itertuples(index=False):
    print(row)

"""排序-基础数据"""
# 定义一个字典
data = {
    'brand':['Python','C','C++','C#','Java'],
    'B':[4,6,8,12,10],
    'A':[10,2,5,20,16],
    'D':[6,18,14,6,12],
    'years':[4,1,1,30,30],
    'C':[8,12,18,8,2],
}
# 定义一个索引列表
index = [9,3,4,5,2]
# 使用pd.DataFrame格式化
df = pd.DataFrame(data=data,index=index)

"""按行索引排序"""
# 按行索引升序排序
print(df.sort_index())
print("------------")
# 按行索引降序排序
print(df.sort_index(ascending=False))
"""按列名排序"""
#按列名升序排序
print(df.sort_index(axis=1))
print("------------")
#按列名降序排序
print(df.sort_index(axis=1,ascending=False))
"""按值排序---按单个列的值排序"""
#按列A的值升序排序
print(df.sort_values(by='A'))
print("------------")
#按列A的值降序排序
print(df.sort_values(by='A',ascending=False))
"""按值排序---按多个列的值排序"""
#按列'years','B'的值升序排序
print(df.sort_values(by=['years','B']))
print("------------")
#按列'years','B'的值降序排序
print(df.sort_values(by=['years','B'],ascending=False))

"""去重---drop_duplicate()"""
# 使用pd.DataFrame生成一个二维数组
data = pd.DataFrame({'a':[1,2,3,4],'b':['a','b','b','c']})
# 删除 DataFrame 中的重复行
print(data.drop_duplicates())
# 指定a作为去重的列
print(data.drop_duplicates(subset='a'))
# 指定'a','b'作为去重的列
print(data.drop_duplicates(subset=['a','b']))

"""去重---drop_duplicated()"""
# 使用pd.DataFrame生成一个二维数组
data = pd.DataFrame({'a':[1,2,3,4],'b':['a','b','b','c']})
# 判断每行是否为重复行
print(data.duplicated())

"""去重---dropna()"""
# 使用pd.DataFrame生成一个二维数组
df = pd.DataFrame({'A':[1,2,np.nan,4],'B':[5,np.nan,7,8],'C':[9,10,11,np.nan]})
# 按列删除缺失值
print(df.dropna(axis=1))
# 每行中最少有2个非空值，否则就删除该行
print(df.dropna(thresh=2))
# 按行删除缺失值时，以'A','B'两列为准
print(df.dropna(subset=['A','B']))

"""过滤缺失值"""
# 使用pd.DataFrame生成一个二维数组
data = pd.Series([1,NA,3.5,NA,7])
# 过滤缺失值，并返回结果
print(data.dropna())

"""填充缺失值"""
# 使用pd.DataFrame生成一个二维数组
df = pd.DataFrame(np.random.randn(7,3))
# 按照列插入缺失值NA到二维数组中
df.iloc[:4,1]=None
df.iloc[:2,2]=None
# 返回结果
print(df)
# 为缺失值填充为0
print(df.fillna(0))

"""csv读写文件"""
# 定义一个字典
data = {"Name":['Smith','Parker'],'ID':[101,102],'Language':['Python','JavaScript']}
# 使用pd.DataFrame生成一个二维数组
info = pd.DataFrame(data)
#数据写入csv文件
csv_data = info.to_csv()
# 返回csv文件内容
print('\n CSV String Values:\n',csv_data)

"""excel读写文件"""
# 使用pd.DataFrame生成一个二维数组
info_website = pd.DataFrame({'name':['编程帮','c语言中文网','微学院','92python'],
                             'rank':[1,2,3,4],
                             'language':['PHP','C','PHP','Python'],
                             'url':['www.biancheng.com','c.biancheng.net','www.weixueyuan.com','www.92python.com']})
# 写入excel
writer = pd.ExcelWriter('website.xlsx')
info_website.to_excel(writer)
# 保存文件
writer.save()