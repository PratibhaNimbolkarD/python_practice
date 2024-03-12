import logging
logging.basicConfig(level=logging.INFO , format='%(message)s')
class Student:
    def __init__(self , name , rollno , age):
        self.name = name
        self._rollno = rollno
        self.__age = age
    def __display(self):
        logging.info(f"Hii myself {self.name} {self.__age} years old with rollno {self._rollno} from student class ")

    def displayPrivateData(self):
        self.__display()

class Branch(Student):
    def show(self):
        logging.info(f"My rollno is {self._rollno}")

s1 = Student("Pratibha" , 23 , 10006)
s1.displayPrivateData()