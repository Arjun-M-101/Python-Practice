class parentMethod():
    def public_method(self):
        print("This is a public method")

    def _protected_method(self):
        print("This is a protected method")

    def __private_method(self):
        print("This is a private method")
    
    def access_sameClass(self):
        print("Accessing from the same class:")
        self.public_method()
        self._protected_method()
        self.__private_method()

class childMethod(parentMethod):
    def access_subClass(self):
        print("Accessing from the subclass:")
        self.public_method()  # Accessible
        self._protected_method()  # Accessible
        try:
            self.__private_method()  # Not accessible, will raise an AttributeError
        except AttributeError as e:
            print("Cannot access private method:", e)
            
class otherClass:
    def access_otherClass(self, parent_instance):
        print("Accessing from another class:")
        parent_instance.public_method()  # Accessible
        parent_instance._protected_method()  # Accessible
        try:
            parent_instance.__private_method()  # Not accessible, will raise an AttributeError
        except AttributeError as e:
            print("Cannot access private method:", e)
            
p=parentMethod()
c=childMethod()
o=otherClass()

p.access_sameClass()
c.access_subClass()
o.access_otherClass(p) # We have to pass the instance of Parent 