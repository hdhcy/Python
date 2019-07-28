import pandas as pd
import numpy as np

#merging two df by key/key.(may be used in database)
#simple example
'''
left=pd.DataFrame({'key':['K0','K1','K2','K3'],
                   'A':['A0','A1','A2','A3'],
                   'B':['B0','B1','B2','B3']})
right=pd.DataFrame({'key':['K0','K1','K2','K3'],
                    'C':['C0','C1','C2','C3'],
                    'D':['D0','D1','D2','D3']})

print(left)
print(right)
res=pd.merge(left,right,on='key')#on表示基于key合并
print(res)
'''

#consider two keys
'''
left=pd.DataFrame({'key1':['K0','K1','K1','K2'],
                   'key2':['K0','K0','KO','K1'],
                   'A':['A0','A1','A2','A3'],
                   'B':['B0','B1','B2','B3']})
right=pd.DataFrame({'key1':['K0','K1','K1','K2'],
                    'key2':['KO','K0','K0','K0'],
                    'C':['C0','C1','C2','C3'],
                    'D':['D0','D1','D2','D3']})
print(left)
print(right)

#how=['inner','right','outer','left'] left right表示按照左边 右边的df进行合并，右边 左边没有的用NaN来表示
res=pd.merge(left,right,on=['key1','key2'],how='left')#默认为inner,即合并相同的项
print(res)
'''

#indicator
'''
df1=pd.DataFrame({'col1':[0,1],
                  'col_left':['a','b']})
df2=pd.DataFrame({'col1':[1,2,2],
                  'col_right':[2,2,2]})

print(df1)
print(df2)

res=pd.merge(df1,df2,on='col1',how='outer',indicator=True)#indicator表示merge合并的方式，默认为False
print(res)
#give the indicator a custom name
res=pd.merge(df1,df2,on='col1',how='outer',indicator='indicator_column')

'''
#merge by index
'''
left=pd.DataFrame({'A':['A0','A1','A2'],
                   'B':['B0','B1','B2']},
                  index=['KO','K1','K2'])
right=pd.DataFrame({'C':['C0','C2','C3'],
                    'D':['D0','D2','D3']},
                   index=['K0','K2','K3'])

print(left)
print(right)
#left_index and right_index
res=pd.merge(left,right,left_index=True,right_index=True,how='outer')#同时考虑两个index
print(res)
'''

#handle overlapping
boys=pd.DataFrame({'k':['K0','K1','K2'],
                   'age':[1,2,3]})
girls=pd.DataFrame({'k':['K0','K0','K3'],
                    'age':[4,5,6]})
print(boys)
print(girls)
res=pd.merge(boys,girls,on='k',suffixes=['_boy','_girl'],how='outer')#表示解决重复的列标识，加上_boy和_girl
print(res)

#join