import pandas as pd

df = pd.read_csv('Main/data2.csv')
print(df)

df2 = df.to_json()
print(df2)

df3 = df['Age'].to_json()
print(df3)