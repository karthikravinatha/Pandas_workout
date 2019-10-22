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

