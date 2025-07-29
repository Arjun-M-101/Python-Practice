def user_profile(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")
user_profile(name="Arjun", age=25, location="India")