class Animal():
    name = "Rahul"
    def a(self):
        print("I am inside animal class")

# inheriting Animal class to Mammal class
class Mammals(Animal):
    def b(self):
        print("I am inside mammals class")

# creating obj of Mammals class
m = Mammals()
m.a()
m.b()
print("Animal class variable :",m.name)

# Multiple inheritance is allowed in python

print("**********************************************************")

class parent():

    def __init__(self,num1,num2,operation):
        self.num1 = num1
        self.num2 = num2
        self.operation = operation

    def  sum(self):
        return "Operation is :",self.operation," :",self.num1 + self.num2

p = parent(100,100,"sum")
print(p.sum())

print("**********************************************************")
# child class is inheriting parent class
class child(parent):

    def __init__(self,num1,num2,operation):
        super().__init__(num1,num2,operation)

c = child(200,200,"sum")
print(c.sum())





