import matplotlib.pyplot as plt
import csv

months=[]
sales=[]

with open ("Main/data.csv","r") as file:
    Data=csv.DictReader(file)
    for row in Data:
        months.append(row['Month'])
        sales.append(int(row['Sales']))
        
plt.plot(months,sales,marker='o')
plt.title("Monthly Sales Report")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.savefig("matplotlib_plot.png")
plt.tight_layout
plt.show()