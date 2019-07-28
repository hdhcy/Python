import pandas as pd
import numpy as np

datas=pd.date_range('20190101',periods=6)
df=pd.DataFrame(np.arange(24).reshape((6,4)),index=datas,columns=['A','B','C','D'])

print(df)

print(df['A'],df.A)#输出第A列，两种方式,好像又不能使用行标识单独输出

print(df[0:3],df['2019-01-02':'2019-01-04'])#输出第零行到第三行，左闭右开，两种方式

#select by label:loc 这种方式通过标签来进行选择 纯标签的筛选
print(df.loc['20190101'])#打印出来这一行的数据
print(df.loc[:,['A','B']])#输出所有行但是列标签只为A和B的数据
print(df.loc['20190103',['A','B']])

#select by position: iloc 根据位置来进行选择 纯数字的筛选
print(df.iloc[3])#输出第三行的数据
print(df.iloc[3,1])#输出第三行第一位的数据
print(df.iloc[3:5,1:3])#输出第三行到第五行，第一列到第三列的数据，均为左闭右开
print(df.iloc[[1,3,5],[1,3]])#不进行连续的筛选，对想要的行数和列数进行筛选

#Boolean indexing 通过boolean的判断进行筛选
print(df)
print(df[df.A>8])#输出标签A中大于8的所有数字，同时显示其他所有的数据
print(df[df.A<8])

