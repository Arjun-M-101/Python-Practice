# FIND THE SUM OF PRICES OF ITEMS WHICH COSTS MORE THAN 1,000
from functools import reduce
items = {
    "book":400,
    "laptop":50000,
    "bottle":200,
    "controller":1500
}
prices=list(items.values())
costly=list(filter(lambda x:x>=1000,prices))
total=reduce(lambda a,b:a+b,costly)
print("The sum of prices of items which costs more than Rs. 1,200:",total)