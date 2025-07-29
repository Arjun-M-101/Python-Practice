class Classroom: 
    def Student(self):
        print("Hi! I'm a student in the classroom.")
object=Classroom()
object.Student() #object.Student() calls the Student method of the Classroom class by passing the object as an argument.

#So whenever we call the method of the class using the object, 
#it automatically passes the object as the first argument to the method.
#So the 'Self' parameter is passed in order to access the attributes and methods of the class which corresponds to the object.