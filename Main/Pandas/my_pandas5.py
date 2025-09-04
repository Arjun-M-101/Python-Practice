import pandas as pd

# Customers Table
customers = pd.DataFrame({
    'CustomerID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie']
})

# Orders Table
orders = pd.DataFrame({
    'OrderID': [101, 102, 103, 104],
    'CustomerID': [1, 2, 1, 3],
    'Product': ['Shirt', 'Pant', 'Shoes', 'Hat']
})

result = pd.merge(customers,orders,on='CustomerID',how='inner')
print("Inner Join: ")
print(result)