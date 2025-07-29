class Dad():
    def home(self):
        print("Daddy's home")
class Son(Dad):
    def factory(self):
        print("Son's factory")
    def home(self):
        print("Son modifies Daddy's home")
result = Son()
result.factory()  # This will print "Son's factory"
result.home()  # This will get home method from Son, which overrides Dad's home method.

# This is an example of method overriding in inheritance, where the child class (Son)
# This is also called polymorphism, where the same method name behaves differently based on the object type.
# So, method overriding is a way to achieve polymorphism in inheritance.