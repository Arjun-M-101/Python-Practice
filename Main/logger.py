'''
def divide(a, b):
    print(f"Dividing {a} by {b}")
    try:
        result = a / b
        print(f"Result: {result}")
        return result
    except ZeroDivisionError:
        print("Error: Tried to divide by zero!")
        return None

# Test
divide(a=10, b=2)
divide(a=10, b=0)
'''
# Configure logging
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app.log',  # You can remove this line to log to console
    filemode='w'
)

def divide(a, b):
    logging.info(f'Dividing {a} by {b}')
    try:
        result = a / b
        logging.debug(f'Result: {result}')
        return result
    except ZeroDivisionError:
        logging.error('Tried to divide by zero!')
        return None
    
divide(a=10, b=2)
divide(a=10, b=0)