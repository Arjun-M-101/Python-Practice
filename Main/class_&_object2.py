class Calculator:
    def square(self, num):
        return num*num
    def cube(self, num):
        return num*num*num
object = Calculator()
print(object.square(5))  # Output: 25
print(object.cube(5))    # Output: 125