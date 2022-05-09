class Person():
    """docstring for Person"""

    def __init__(self, fname, lname):
        super(Person, self).__init__()
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome ", self.fname, self.lname,
              "to the class of", self.graduationyear)


x = Student("Mike", "Olsen", 2019)
x.welcome()
