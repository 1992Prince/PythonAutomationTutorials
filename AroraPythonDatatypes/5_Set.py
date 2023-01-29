"""
SET :
  1. It is similar to list
  2. It can store diff type of values or objects
  3. Set can't have duplicate (List can have)
  4. Set are defined using {} curly braces
  5. It's a collection which is unordered and unindexed
  6. We can't access set elements via indexing
"""

set1 = {"Selenium","Appium","Cypress",100,True,100.1}
print("set1",set1," type of set1 :",type(set1)," length of set :",len(set1))

# iteration
for i in set1:
    print(i)

# adding new element in Set
set1.add("Protractor")
print("updated set1 :",set1)

# removing element from Set
set1.remove("Cypress") # set1.discard("Cypress") will also do the same operation
print("Set after removal of element :",set1)

# remove() vs discard()

