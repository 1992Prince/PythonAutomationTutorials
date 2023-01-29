"""
Tuples
  1. It is used to store sequence of Immutable objects
  2. Mostly all other operations are similar to list
  3. represented by ()
  4. We can't change existing tuple since tuples are immutable
     or we can't reassign values to tuple
  5: We can't delete any item from tuple since tuples are immutable
"""

# Tuple slicing
t1 = (0,1,2,3,4,5)
print("t1[0:] ",t1[0:])   #t1[0:]  (0, 1, 2, 3, 4, 5)
print("t1[:] ",t1[:])     #t1[:]  (0, 1, 2, 3, 4, 5)
print("t1[2:4] ",t1[2:4]) #t1[2:4]  (2, 3)
print("t1[:4] ",t1[:4])   #t1[:4]  (0, 1, 2, 3)
print(t1[3])              # 3


"""
Tuple Operations
  1. Repetation
  2. Concatenation
  3. Membership Operation
  4. Iteration
"""

t3 = (1,"Rahul")
print("t3 * 2 :",t3*2) #(1, 'Rahul', 1, 'Rahul')

print("*********************************************")
t4 = (2,"Cory")
print("t3 + t4 :",t3+t4) #(1, 'Rahul', 2, 'Cory')

print("*********************************************")
print("Rahul" in t3) # True
print("Rahul1" not in t3) # True

print("*********************************************")
# Iterating tuples
for i in (1,2,3,4,5):
    print(i)




