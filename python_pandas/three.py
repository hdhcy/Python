import pandas as pd
import numpy as np

datas=pd.date_range('20190101',periods=6)
df=pd.DataFrame(np.arange(24).reshape((6,4)),index=datas,columns=['A','B','C','D'])

print(df)
df1=df.copy()
df2=df.copy()

df1[df1.A>4]=0#更改所有的A>4的值，包括B C D 中的值
print(df1)

df2.A[df2.B<7]=0#这样书写只对A这个标签列中的内容进行修改条件为B这个标签中小于7的数字所在的行，不会改变B C D 中的值
print(df2)

df['F']=np.nan#新增一个F标签列，值全为nan，即NONE
df['E']=pd.Series([1,2,3,4,5,6],index=pd.date_range('20190101',periods=6))#这种方式新增数列要注意要与原先的行标签一致，不一致的话，默认为NaN，寻找最开始的相同行标签的，并且从series的第一个值开始

print(df)
