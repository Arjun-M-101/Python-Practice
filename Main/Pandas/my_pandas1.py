import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Mumbai']
}

df = pd.DataFrame(data)
print(df)

print(df['Age'])

print(df.dtypes)