class Dad():
    def home(self):
        print("Daddy's home")
class Mom():
    def savings(self):
        print("Mommy's savings")
class Daughter(Dad, Mom):
    def textile_shop(self):
        print("Daughter has textile shop")
class Son(Dad, Mom):
    def factory(self):
        print("Son has factory")
Daughter_asset = Daughter()
Daughter_asset.home()  # Because Daughter inherits from Dad, so she can access the home (method).
Daughter_asset.savings()  # Daughter also has access to Mommy's savings (method).
Daughter_asset.textile_shop()  # Daughter also has her own textile shop (method).

Son_asset = Son()
Son_asset.home()  # Because Son inherits from Dad, so he can access the home (method).
Son_asset.savings()  # Son also has access to Mommy's savings (method).
Son_asset.factory()  # Son also has his own factory (method).

# This is called multiple inheritance,
# where multiple child classes (Daughter and Son) inherit from multiple parent classes (Dad and Mom).