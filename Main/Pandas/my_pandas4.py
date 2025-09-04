import pandas as pd

df = pd.read_json('Main/data3.json')
print(df)

df2 = df.to_csv(index=False)
print(df2)