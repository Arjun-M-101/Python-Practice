def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError: # <--- If you know mention the exception
        print("Error: Division by zero is not allowed.")
        return None
    except TypeError: # <--- If you know mention the exception
        print("Error: Please provide numbers only.")
        return None
    else:
        return result

try:
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))
    c = divide(a, b)
    print("Result:", c,"\n")
except Exception: # <--- We can mention like this 'Exception'
    # if we don't know the specific exception
    print("Error: Please enter valid integers only.\n")
finally: # This will always execute regardless of exceptions
    print("Note: To get accurate results, users are requested to provide valid input for division operations.\n")