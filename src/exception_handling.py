import logging

logging.basicConfig(level=logging.INFO , format='%(message)s')

try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    result = x / y
    logging.info("Result: %s", result)
except ValueError:
    logging.error("Please enter valid numbers.")
except ZeroDivisionError:
    logging.error("Cannot divide by zero.")
except Exception as e:
    logging.error("An error occurred: %s", e)
