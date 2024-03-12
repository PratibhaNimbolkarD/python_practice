import logging
logging.basicConfig(level=logging.INFO , format='%(message)s')
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x ,y):
    return x/y


def calculator(func , num1 , num2):
     return func(num1 , num2)


logging.info(calculator( sub , 5 ,4))