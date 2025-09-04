import pandas as pd

df = pd.read_csv('Main/sales.csv')
print(df)

df['Total'] = df['Price']*df['Quantity']

df.merge(df['Total'])
print(df)

group_df = df.groupby('Product')['Total'].sum().reset_index()

sorted_df = group_df.sort_values(by='Total',ascending=False)

print(sorted_df)