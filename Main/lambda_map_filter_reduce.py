# lambda syntax - argument : expression
# map syntax - map(lambda argument:operation,items) - it iterates over the items without loop
letters=["a","b","c","d"]
upper_letters=list((map(lambda letter:letter.upper(),letters)))
print(upper_letters)

# filter syntax - filter(lambda argument:operation,items) - it iterates until the condition is satisfied
nums=[1,2,3,4,5,6,7,8,9,10]
even=list(filter(lambda num:num%2==0,nums))
print(even)

from functools import reduce # - we need to import reduce from functools to use it
# reduce syntax - reduce(lambda argument:operation,items) - it iterates until it reduces the result to one
total=reduce(lambda a,b:a+b,nums)
print(total)