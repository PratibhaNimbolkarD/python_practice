import logging

logging.basicConfig(level=logging.INFO ,format='%(message)s')

try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    result = x / y
    logging.info("Result: %s", result)
except ValueError:
    logging.error("Please enter valid numbers.")
except ZeroDivisionError:
    logging.error("Cannot divide by zero.")
else:
    logging.info("No exceptions occurred.")
finally:
    logging.info("Exiting the program.")
