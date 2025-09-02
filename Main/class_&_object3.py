class ID_Creation:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def id_card(self):
        return f"ID Card has been created for {self.name}"
    def id_details(self):
        return f"ID details:\nName: {self.name}\nAge: {self.age}"
object=ID_Creation("Arjun", 23)
print(object.id_card())
print(object.id_details())