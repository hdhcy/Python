import pandas as pd

data=pd.read_csv('C:\\Users\\98276\\Documents\\student.csv')
print(data)

data.to_pickle('C:\\Users\\98276\\Documents\\student.pickle')