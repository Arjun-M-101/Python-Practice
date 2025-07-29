# Composed function - When output of one function is passed as input for another function
def add(x):
    return x + 2
def multi(x):
    return x * 2
def mixed(x):
    return add(multi(x)) # - Like this
print(mixed(2))