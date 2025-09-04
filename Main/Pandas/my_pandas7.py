import pandas as pd

# Specify header=None and pass column names
df = pd.read_csv('Main/data3.csv', header=None, names=['Name', 'Age', 'City'])

print(df)