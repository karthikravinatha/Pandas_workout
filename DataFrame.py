import pandas as pd

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)
print(frame)
print(frame.head())

#rearrangement the columns
print(pd.DataFrame(data,columns=['year','state','pop']))

obj1 = pd.DataFrame(data,columns=['pop','state','year','gender'],index=['one','two','three','four','five','six'])
print(obj1)
print(obj1.columns)

#to get data column wise
print(obj1['state'])

#retreiving data by row wise specifiying index id
print(obj1.loc['three'])

lst = [{'a': 1, 'b': 2, 'c':3}, {'a': 4, 'b':5, 'c':6, 'd':7},{'a':6,'b':5,'e':10}]
df = pd.DataFrame(lst)
print(df)

lst1 = [{'a':15,'b':20,'c':25}]
df1 = pd.DataFrame(lst1)
print(df1)

# lst2 = [[1,2,3],[10,20,30]]
# ix = [['a','b','c']]
# df2 = pd.DataFrame(data=lst2,columns=ix)
# print(df2)

#Although the following command will work, we have less control over our NaN value.
data_val = [[1,2],[4,5]]
data_col = ['a','b']
df3 = pd.DataFrame(data=data_val,columns=data_col)
print(df3)


