# Partial function is used when we need to pass only few arguments to function without all arguments mandatorily
from functools import partial
def email_generator(username,domain):
    return f"{username}@{domain}.com"
gmail=partial(email_generator,domain="gmail")
ymail=partial(email_generator,domain="ymail")
print(gmail("gokul"))
print(ymail("pritha"))