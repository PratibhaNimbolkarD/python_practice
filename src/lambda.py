import logging
logging.basicConfig(level=logging.INFO , format= '%(message)s')

numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x ** 2, numbers)
logging.info(list(squared_numbers))