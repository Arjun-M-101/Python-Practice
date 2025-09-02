# Call function is a function that we pass as argument to another function, so that it can be executed later,
# Usually after some action is completed

def print_me_baby(message):
    print("Thanks for clicking me uWu. Here's your message: ")
    message()
def show_message():
    print("Hi mame! Epdi irukka?")
print_me_baby(show_message)