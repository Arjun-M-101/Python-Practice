# generator function with yield is used when we want to return the value one by one without returning all at once
def num_generator1(n):
    return (i for i in range(n))
def num_generator(num):
    for i in range(num):
        yield i
# The values will be yielded to num_generator. Now, we can get the data one by one using for loop
for i in range (5):
    print(i)