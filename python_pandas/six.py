import pandas as pd
import numpy as np

#concatenating

df1=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
df2=pd.DataFrame(np.ones((3,4))*1,columns=['b','c','d','e'])
df3=pd.DataFrame(np.ones((3,4))*2,columns=['a','b','c','d'])

#join,['inner','outer']
'''
res1=pd.concat([df1,df2],join='outer')#join默认为outer处理模式，全部合并，两个数据矩阵之前没有的东西，用NaN来表示
res2=pd.concat([df1,df2],join='inner')#join设置为inner处理模式，合并相同的项目
res3=pd.concat([df1,df2],join='inner',ignore_index=True)#ignore_index表示将处理的行序号进行排列,从零开始，为False的话，默认不排序
'''

#join_axes
'''
df1=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'],index=[1,2,3])
df2=pd.DataFrame(np.ones((3,4))*1,columns=['b','c','d','e'],index=[2,3,4])
a=pd.concat([df1,df2],axis=1,join_axes=[df1.index])#aixs=1表示左右合并，axis=0表示上下合并，join_axes表示按照df1的索引进行合并
b=pd.concat([df1,df2],axis=1)#同时考虑两者，进行合并，没有的index用NaN来表示

print(b)
'''

#append
df1=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
df2=pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
df3=pd.DataFrame(np.ones((3,4))*1,columns=['b','c','d','e'],index=[2,3,4])

res=df1.append(df2,ignore_index=True)#默认axis等于0，表示竖向的添加数据
res1=df1.append([df2,df3])#可以同时囊括两个
s1=pd.Series([1,2,3,4],index=['a','b','c','d'])
res2=df1.append(s1,ignore_index=True)#还是在下方添加

print(res2)
