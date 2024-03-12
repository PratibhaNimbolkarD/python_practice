import logging
logging.basicConfig(level=logging.INFO , format= '%(message)s')
class Human:
    def eat(self):
        logging.info("I can eat")
    def work(self):
        logging.info("I can work")

class Male(Human):

    def walk(self):
        logging.info("I can walk")

    def work(self):
        super().work()
        logging.info("I can code")

First_male = Male()
First_male.eat()
First_male.work()
First_male.walk()