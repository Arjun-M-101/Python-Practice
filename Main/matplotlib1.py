import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y)
plt.title("Simple Line Plot")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()

import matplotlib.pyplot as plt

x = ['Apple', 'Banana', 'Grapes']
y = [30, 15, 45]

plt.bar(x, y, color='green')
plt.title("Fruit Count")
plt.ylabel("Count")
plt.show()

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [5, 20, 15, 25, 10]

plt.scatter(x, y, color='red')
plt.title("Simple Scatter Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()