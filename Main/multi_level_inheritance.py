class Grandpa():
    def car(self):
        print("Grandpa has Lamborghini")
class Dad(Grandpa):
    def home(self):
        print("Daddy has home")
class Son(Dad):
    def factory(self):
        print("Son has factory")
asset=Son() #This object tell that Son can inherit from Dad and also has access to Grandpa's car.
asset.car()  # Because Son inherits from Dad, so he can access the car (method) from Grandpa.
asset.home() #Because Son inherits from Dad, so he can access the home (method).
asset.factory() #Son also has his own factory (method).

#This is called multi-level inheritance, where one class (Son) inherits from another parent class (Dad) 
#which also has access to the properties and methods of its parent class (Grandpa). 
#Therefore, the child class can access all the methods and properties of its parent classes in a chain.