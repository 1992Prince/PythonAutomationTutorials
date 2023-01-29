"""
Polymorphism :

 1. Operator Overloading
 2. Method Overloading/Method Overriding
 3. Constructor Overloading/Constructor Overriding

 Note : Method Overloading is not possible in case of python
        if we have two methods with same name with diff params in same class, then
        latest method written will be considered as final method def and we can't count
        both methods as 2 diff methods

        Similar Constructor Overloading is also not possible in python

        Method Overriding is allowed in python, below is an example

"""

class MethodOverridingBase:

    def __init__(self):
        print("Base class constructor")

    def a(self):
        print("Inside Base class")


class MethodOverridingDerived(MethodOverridingBase):

    def __init__(self):
        print("Derived class constructor")
        # calling base class constructor
        super().__init__()

    def a(self):
        print("Inside Derived class")
        # I want to call parent class a() def also
        super().a()

obj = MethodOverridingDerived();
obj.a()