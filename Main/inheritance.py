class Dad():
    def home(self):
        print("Daddy has home")
class Son(Dad):
    def __init__(self, inherit):
        self.inherit = inherit
    def factory(self):
        print(f"Son has factory. {self.inherit}")
key=Son("But daddy's home is also son's home")
key.home() #Because Son inherits from Dad, so he can access the home (method).
key.factory() #Son also has his own factory (method).

#This is called single inheritance, where one class (Son) inherits from another class (Dad).