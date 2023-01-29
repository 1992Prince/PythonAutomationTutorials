"""
3 Types of methods/functions in Python

  1. instance methods : used to access instance variables of class
  2. class methods   : used to access static/class variables
  3. static methods  : standalone methods

"""

class Dog:

    legs = 4

    def __init__(self):
        self.name = "Milo"
        self.color = "Red"

    # below is instance method since it is accessing only instance variables
    # inside instance method we can access class/static variables also
    # we can access only instance methods via class object only
    def getDogName(self):
        print("Instance method",self.name," ",self.color)

    @classmethod
    def getLegsCount(self):
        print("Class Method :",Dog.legs)

    @staticmethod
    def generalInformation():
        print("Beware of dogs")


d = Dog()
# accessing class variable
print("Class Variable :",Dog.legs)
# accessing class method
Dog.getLegsCount()
# accessing instance method
d.getDogName()

# calling static method
Dog.generalInformation()