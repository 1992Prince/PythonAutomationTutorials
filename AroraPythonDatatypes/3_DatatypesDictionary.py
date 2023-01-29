"""
key and value pair
 1: Key : Numbers, String, Tuple (Key will be python immutable objects)
 2: Value : Python Object
"""

D1 = {
    "Name":"Rahul",
    "Age":45
}

print(type(D1)," ",D1," ",D1["Name"])

# Updating values in Dictionary
D1["Name"] = "Sanjeev"
print(type(D1)," ",D1," ",D1["Name"])

print("---------------------------------------")
# printing all key of dictionary
for a in D1:
    print(a)

print("---------------------------------------")
# printing all values of dictionary
for a in D1:
    print(D1[a])

# Another way of printing Dictionary values
print("---------------------------------------")
for c in D1.values():
    print(c)

# Printing Dictionary key and values
# below key and pair will be printed in form of tuple
print("---------------------------------------")
for c in D1.items():
    print(c)

# Dictionary having values as list
print("---------------------------------------")
item = {
    "fruits":["Apple","Mango","Banana"],
    "Price":100,
    "Size":10.5
}

print(item["fruits"])
print(item["fruits"][0])
print(item.get("Size"))

print(len(item))
print(item.keys())