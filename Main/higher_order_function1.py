# This is normal way of writing functions. Not a good practice.
'''
def email_provider (username,domain):
    if domain == "gmail":
        return f"{username}@{domain}.com"
    if domain == "ymail":
        return f"{username}@{domain}.com"
    if domain == "hotmail":
        return f"{username}@{domain}.com"
    
print(email_provider("arjun","gmail"))
print(email_provider("gokul","gmail"))
print(email_provider("pritha","gmail"))
'''

# Higher order function 1 - Takes function as an argument

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