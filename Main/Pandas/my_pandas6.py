import pandas as pd

df = pd.DataFrame({'x': [1, 2, 3, 4, 5]})
result1 = df['x'] > 3  # This runs immediately
print(result1)

result2 = df[df['x'] > 3]  # This runs immediately
print(result2)