"""
List Operations
 1. Repetition operations
 2. Concatenation operations
 3. Membership operations
 4. Iterations
 5. Length function
"""

# Repetition Operation
l1 = [1,2,3,"Rahul",True]
print(l1*2) # [1, 2, 3, 'Rahul', True, 1, 2, 3, 'Rahul', True]

# Concatenation Operation
l2 = [5,6,7,"Cory",False]
print(l1+l2) # [1, 2, 3, 'Rahul', True, 5, 6, 7, 'Cory', False]

# Membership operation
print("Rahul" in l1) # True
print("Cory" in l1)  # False

# Iteration Operation
for i in l1:
    print(i)

# Length function
print("Length of list is :",len(l1))

# max and min values in list
l3 = [1,2,3,4,5,6,7,8,9,10]
print("Max value is :",max(l3))
print("Min value is :",min(l3))

# convert string to list
str1 = "Rahul"
print(list(str1)) # ['R', 'a', 'h', 'u', 'l']


