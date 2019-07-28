import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#plot data

#Series
data=pd.Series(np.random.rand(1000),index=np.arange(1000))

data=data.cumsum()#进行累加
data.plot()

#DataFrame
data=pd.DataFrame(np.random.rand(1000,4),
                  index=np.arange(1000),
                  columns=list('ABCD'))
print(data.head())#输出前三个数据，默认为5个数据
data=data.cumsum()
data.plot()
plt.show()

plt.show()

#plot methods
#'bar' 'hist','box','area','scatter','hexbin','pie'
