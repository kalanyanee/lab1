import pandas as pd
df = pd.read_csv('winequality-red.csv',sep=';')
#print(df)
#print(df.head())
#print(df.tail())
print(df.columns)
print('*****************************************************************')
#print(df.info())
#print(df.shape)
#print(df.describe())
ds1 = df[['citric acid','pH']]
print(ds1)
print('*****************************************************************')
print(df)
print('*****************************************************************')
print(df.iloc[[0,2,3],:])
print('*****************************************************************')
print(df.iloc[range(1,5),[0,2,8]])
#df.loc[df['fixed acidity']>8.0,['fixed acidity','pH']]
print('*****************************************************************')
print(df.loc[df['fixed acidity']>8.0,['fixed acidity','pH']])
df['newcol']=1
print(df)