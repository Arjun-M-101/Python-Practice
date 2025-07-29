class Parent:
    def __init__(self):
        self.public_var = "I am public"
        self._protected_var = "I am protected"
        self.__private_var = "I am private"
        
    def access_from_sameClass(self):
        print(self.public_var)
        print(self._protected_var)
        print(self.__private_var)
        
class Child(Parent):
    def access_from_subClass(self):
        print(self.public_var)  # Accessible
        print(self._protected_var)  # Accessible
        try:
            print(self.__private_var)  # Not accessible, will raise an AttributeError
        except AttributeError as e:
            print("Cannot access private variable:", e)

class AnotherClass:
    def access_from_otherClass(self, parent_instance):
        print(parent_instance.public_var)  # Accessible
        print(parent_instance._protected_var)  # Accessible
        try:
            print(parent_instance.__private_var)  # Not accessible, will raise an AttributeError
        except AttributeError as e:
            print("Cannot access private variable:", e)
            
p=Parent()
c=Child()
a=AnotherClass()

p.access_from_sameClass()
c.access_from_subClass()
a.access_from_otherClass(p) # We have to pass the instance of Parent 
                            # to access its variables from AnotherClass.