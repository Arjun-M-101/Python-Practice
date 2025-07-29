class Order:
    def __init__(self, customer_name, items, total_amount, discount):
        self.customer_name = customer_name
        self.items = items
        self.__total_amount = total_amount
        self.__discount = discount
        
    def __bill(self): # This is a private method, not accessible outside class Order.
        # But this can access other private attributes of the class Order.
        return self.__total_amount - self.__discount # Created separately to hide from customer.

    def _get_admin_view(self): # This is a protected method, 
        # can access the private attributes of the class Order since they're called in this.
        # it can access the private method __bill() because it is within the same class.
        return {
            "Customer Name": self.customer_name,
            "Items": self.items,
            "Total Amount": self.__total_amount,
            "Discount": self.__discount,
            "Final Bill": self.__bill()
        }
        
    def get_customer_view(self): # This is a public method, accessible to everyone.
        # It can access the private method __bill() because it is within the same class.
        return {
            "Customer Name": self.customer_name,
            "Items": self.items,
            "Final Bill": self.__bill()
        }
        
class AdminPortal():
    def view_order(self,order):
        return order._get_admin_view() # This means - We are getting only the admin view 
    # of the order. Means only certain values stored in the __init__ method as per admin view.
    # Since _get_admin_view() already has access to the values of class Order & bill, it easily
    # returns the admin view.

# Or in other words, we are creating this AdminPortal class to get access to the 
# _get_admin_view() method, which inturn could access the __bill() and private 
# attributes of class Order. Because we cannot access the private attributes directly 
# from outside the class Order.

class CustomerPortal():
    def view_order(self,order):
        return order.get_customer_view() # This means - We are getting only the customer view 
    # of the order. Means only certain values stored in the __init__ method as per customer view.
    # Since get_customer_view() already has access to some values of class Order & bill, it easily
    # returns the customer view.

# Or in other words, we are creating this CustomerPortal class to get access to the 
# get_customer_view() method, which inturn could access the __bill() and public 
# attributes of class Order. Because we cannot access the private attributes directly 
# from outside the class Order.

order=Order("Arjun", ["Chicken Samosa", "Paneer Tikka"], 1000, 100)
admin=AdminPortal()
customer=CustomerPortal()
print(admin.view_order(order))  # Admin can see all details including total amount and discount. 
print(customer.view_order(order))  # Customer can only see their name, items, and final bill.
# This demonstrates encapsulation, where sensitive data (total amount and discount) 
# is hidden from the customer.

print(Order.__dict__['__discount'])  # This will raise an AttributeError, as __discount is private.