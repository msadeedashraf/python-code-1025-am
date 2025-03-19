# Python Inheritance
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(f"My name is {self.firstname} {self.lastname}")


# Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

y = Person("Arash", "Usmani")
y.printname()


# student class inherits Person Class
class Student(Person):
    pass


a = Student("Kennedy", "Madangombe")
a.printname()
