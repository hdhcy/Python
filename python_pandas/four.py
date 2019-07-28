import pandas as pd
import numpy as np

datas=pd.date_range('2019-01-01',periods=6)
cols=['A','B','C','D']
df=pd.DataFrame(np.arange(24).reshape((6,4)),index=datas,columns=cols)

df.iloc[0,1]=np.nan
df.iloc[1,2]=np.nan
print(df)

df1=df.copy()
df2=df.copy()

print(df1.dropna(axis=0,how='any'))#axis={1，0} 0表示行,1表示列，how={'any','all'} any表示这一行中只要有一个值为NaN，就把这一行丢掉，all表示只有这一行中所有的值都为NaN的时候才把这一行丢掉，默认情况为any

print(df2.fillna(value=0))#对NaN的值进行填入，value表示要填入的值

print(df.isna(),df.isnull())#两值都可以对值进行是否为NaN的判断

print(np.any(df.isnull())==True)#这个数据表格中至少有一个值为NaN
