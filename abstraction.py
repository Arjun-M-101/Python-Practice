from abc import ABC, abstractmethod

class Feature(ABC):
    @abstractmethod
    def login(self):
        pass
    
    @abstractmethod
    def two_factor_authentication(self):
        pass
    
    def buy_item(self):
        pass
    
class App(Feature):
    def login(self):
        return "Login successful"
    
    def two_factor_authentication(self):
        return "Two-factor authentication successful"
    
#    def buy_item(self):
#        return "Item purchased successfully"
    
Deployment = App()
print(Deployment.login())  # Accessing login method
print(Deployment.two_factor_authentication())  # Accessing two-factor authentication method
#print(Deployment.buy_item())  # Accessing buy item method