"""
Constructors :

They are called first function of class

syntax : __init__()

All classes have this function which is always executed when the class is being
initiated or an object of class is created

"""

class Practice:

    def __init__(self):
        print("I am the constructor bro!!!")

    def add(self):
        print("Adding something")

# creating obj of class and constructor will be executed
p = Practice()
p.add()

print("**************************************************")

class Emp:

    # company is class variable and we can access it with either self of class name
    company = "Microsoft"
    # inside constructor we define instance variables wch will be common to all class objects
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def display(self):
        print("Name is :",self.name," Id is :",self.id," Company is :",Emp.company) # self.company

e = Emp("Prince",145634)
e.display()