# Higher order function 1 - Takes function as an argument
'''
def gmail(username, domain="gmail"): # 5 - So based on the domain function provided in the input it choses
    return f"{username}@{domain}.com" # And returns the email address
def ymail(username, domain="ymail"):
    return f"{username}@{domain}.com"
def hotmail(username, domain="hotmail"):
    return f"{username}@{domain}.com"

def email_provider(username, email_function): # 3 - Parameters are passed here
    return email_function(username) # 4 - The email_function here corresponds to the domain function provided before

print(email_provider("arjun", gmail)) # 1 - email_provider function is called
print(email_provider("gokul", ymail)) # 2 - It passes the username & calls email_function
print(email_provider("pritha", hotmail))
'''

# Higher order function 2 - Returns functions as output
def email_provider(domain): # Outer function just takes the domain
    def email_builder(username):
        return f"{username}@{domain}.com"
    return email_builder # The idea is we keep the logic inside inner function - Here builder

# These are context boundary or pre-bound logic        
gmail=email_provider("gmail") # The outer functions passes the 'domain' and executes inner function
ymail=email_provider("ymail")
hotmail=email_provider("hotmail")

print(gmail("arjun")) # This function call passes the 'username' for the inner function
print(ymail("gokul"))
print(hotmail("pritha"))