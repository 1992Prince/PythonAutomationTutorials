
def print_my_name():
    print("My name is Rahul Arora")

print_my_name()

print("****************************************")

def print_my_parametrised_name(name):
    print("My parametrised name is :",name)

print_my_parametrised_name("Krishna")

print("****************************************")

def print_my_returned_name(name):
    return "My returned name is :"+name

print(print_my_returned_name("Hanuman"))

print_my_parametrised_name("Krishna")

print("****************************************")

def get_user_details(name,age,salary): # here name, age, salary are called formal parameters
    print("Name is :",name," Age is :",age," Salary is :",salary)

get_user_details("Prince",30,100000000) # here Prince, 30, 1 million are called arguments

print("****************************************")

"""
Types of Arguments

 1. Required Arguments
 2. Keyword Arguments
 3. Default Arguments
 4. Variable length Arguments
 
"""

