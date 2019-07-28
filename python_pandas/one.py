import pandas as pd
import numpy as np

s=pd.Series([1,2,3,4,5,np.nan,6])
#在pandas中的数字是float64或者float32位的格式来保存
print(s)

datas=pd.date_range('20190101',periods=6)#生成一个从2019-01-01开始的连续的六个日期，同时要注意日期范围
print(datas)

df=pd.DataFrame(np.random.rand(6,4),index=datas,columns=['a','b','c','d'])#随机生成一个6行4列的矩阵，其中行index用日期来定义，列columns用a,b,c，d来定义
print(df)

df1=pd.DataFrame(np.random.rand(6,4))#默认0 1 2 3 4 5 为行的序列，0，1，2，3 为列的序列
print(df1)

#同时也可以用字典格式进行创建
df2=pd.DataFrame({'A':1.,
                  'B':pd.Timestamp('20130102'),
                  'C':pd.Series(1,index=list(range(4)),dtype='float32'),
                  'D':np.array([3]*4,dtype='int32'),
                  'E':pd.Categorical(['test','train','test','train']),
                  'F':'foo'})#这样写的话，要保证数据一样长，A,B,C,D,E,F表示列的标识
print(df2)
print(df2.dtypes)

print(df2.index)#输出行的的标识
print(df2.index.dtype)#输出行的的标识的类型
print(df2.columns)#输出列的标识
print(df2.values)#输出所有的值，values

print(df2.describe())#describe()只能对数字进行计算他们的平均值，个数，方差等数学属性

print(df2.T)#对矩阵进行翻转

print(df2.sort_index(axis=1,ascending=False))#对列的名称进行排序,ascending表示排序的类型，False表示倒序，Ture表示正序

print(df2.sort_index(axis=0,ascending=False))#对行的名称进行排序,ascending表示排序的类型，False表示倒序，Ture表示正序

print(df2.sort_values(by='E',ascending=False))#对列标识为E进行排序，ascending表示排序的类型，False表示倒序，Ture表示正序

#sort_values只能对列进行排序，