class MyClass:
    Dialogue="Hi mame!"
    def instance_method(self):
        return "Hi! I'm an instance method."
    
    @classmethod
    def class_method(cls,new_dialogue):
        cls.Dialogue=new_dialogue
        return f"Hi! I'm a class method. The new dialogue is: {cls.Dialogue}"

    @staticmethod
    def static_method(a, b, message):
        sum = a + b
        Dialogue = message
        return f"Hi! I'm a static method. The sum is: {sum}. The new dialogue is: {Dialogue}"

object=MyClass()
print("My dialogue is:",object.Dialogue)
print("After calling instance method:",object.instance_method(),"\n")  # Calling instance method

print("My dialogue is:",MyClass.Dialogue)
print("After calling class method:",MyClass.class_method("Maja Akkov Idhu!"),"\n")  # Calling class method
# If you notice, you can see that class_method can access the class-level attribute 'Dialogue'
# This shows that class method can modify class-level attributes
# Here you can see that the class-level attribute 'Dialogue' is modified by the class method.

print("My dialogue is:",MyClass.Dialogue)
print("After calling static method:",MyClass.static_method(5, 10, "Maja pa idhu!"),"\n")  # Calling static method
# Here, you can notice that the dialogue modified by class_method is still present.
# But it does not have access to the actual class-level attribute 'Dialogue'.
# Its because static method never interacts with class-level attributes.
# Even though it prints the dialogue, it does not change the class-level attribute 'Dialogue'.
# It's only its own local variable 'Dialogue' that is printed.
# It performs only its own task like calculating the sum of two numbers.

# THE MAIN DIFFERENCE IS INSTANCE METHOD CAN BE CALLED BY CREATING AN OBJECT OF THE CLASS,
# BUT EHT CLASS & STATIC METHODS CAN BE CALLED DIRECTLY USING THE CLASS NAME.