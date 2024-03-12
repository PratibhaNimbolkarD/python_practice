import logging
logging.basicConfig(level=logging.INFO , format='%(message)s')
def print_sum(first , second) :
    return first+second


first = int(input("Enter the first number : "))
second = int(input ("Enter the second number : "))
logging.info(print_sum(first , second))
