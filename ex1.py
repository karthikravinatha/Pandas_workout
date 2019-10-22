import pandas as pd
import numpy as np
from pandas import Series,DataFrame

obj = pd.Series([10,20,30,40,50,60,70,80,90])
print(obj)
print(obj.shape)
print(obj.values)

obj1 = pd.Series(['hello','karthik','where','are','you'])
print(obj1)
print(obj1.values)
print(obj1.index)

obj2 = pd.Series([12,30,45,60,75,90],index = ['a','b','c','d','e','f'])
print(obj2)
print(obj2.index)
print(obj2[['a','b','c']])

#Using NumPy functions or NumPy-like operations, such as filtering with a boolean array#
print(obj2[obj2 == 15])
print(obj2[obj2 < 30])
print(obj2[obj2 != 45])
print(obj2 * 2)
print(np.exp(obj2))
print('c' in obj2)

#data contained in a Python dict
data = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
state = ['karnataka','tamilnadu','goa','Utah']
print(pd.Series(data))
obj3 = pd.Series(data,index=state)
print(obj3)
print(pd.isnull(obj3))


