# A recursive function is a function which calls itself until it solves the smaller version of its same problem
# Factorial using recursion
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
print(factorial(5))
# Countdown
def bomb(n):
    if n == 0:
        return "Boom!"
    print(n)
    return bomb(n-1)
print(bomb(5))