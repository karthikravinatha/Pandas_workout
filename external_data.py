import pandas as pd

# load data in from a CSV, we would simply use:
df1 = pd.read_csv('winequality-red.csv', delimiter=';')

# we have the column names in the first row of our .csv file. If our file did not have column headings, we could read in our data in the following way:
df2 = pd.read_csv('winequality-red.csv', header=None)

# remane our columns upon reading in our data using the names argument:
df = pd.read_csv('winequality-red.csv', header=None,
                 names=['col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7', 'col8', 'col9', 'col10', 'col11',
                        'col12'])
# print(df1)
# print(df1.shape)
print(df1.columns)  # displays columns names
# print(df1.info)
# print(df1.describe)
print(df1.head())  # first 5 records
print(df1.tail())  # last 5 records
print(df1['alcohol'])  # display perticular column data
print(df1.chlorides)  # display perticular column data

# loc
k1 = df1.loc[0, ['sulphates']]
print(k1)

# #iloc
# k2 = df1.iloc[:10,5:]
# print(k2)

#filtering the values by requitment
s1 = df1.loc[df1['alcohol']<=9]

s2 = s1.iloc[:5,:2]
print(s2)
print(df1.shape)

a= [[1],[2,3],[4]]
print(sum(a,[]))

b = df1[(df1['alcohol'] > 9 ) & (df1['alcohol']<10)]
print(b)

c = df1['quality'].unique()
print(c)

d = df1.groupby('quality').mean()
print(d)

e = df1.groupby('quality').max()
print(e)

f = df1.groupby('quality').std()
print(f)

df1 = df1.eval('total = sulphates + alcohol')
print(df1)

df1 = df1.drop(columns='total',axis=True)
print(df1)



