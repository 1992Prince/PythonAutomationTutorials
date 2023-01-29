"""
  1. List
  2. Tuple
  3. Dictionary

"""

"""
List - Data Type
 1. It is just a consective collection of related items/words
 2. Represents a group of values as a single entity, order is very important
 3. It allows duplicate values as well
 4. represented by []
 5. Values are seperated by comma
 6. Order is preserved
 7. List allows duplicate values
 8. we can fetch element by index
 9. List is mutable i.e. we can add more elements to list
 10. Immutable means we can't modify existing list
"""

a = [] #empty list
b = [1,2,3,"Rahul",True]
print(type(b)," ",b)

# List slicing
print("list slicing b[0:] :",b[0:])
print("list slicing b[:] :",b[:])
print("list slicing b[2:4] :",b[2:4])
print("list slicing b[:4] :",b[:4])

# length of list
print("Length of list is :",len(b))

# Using slicing operation to update list
b[2:4] = ["Arjun","Karna","Kunti Putra"]
print("Updated list is :",b)

# Deleting the list element
del b[4]
print("List after deleting :",b)

# sort list
d = [11,15,1,5,4]
e = ['z','m','a','p','s']
d.sort(reverse=True)
e.sort()
print("Reverse sorted order is :",d)
print("sorted order is :",e)

