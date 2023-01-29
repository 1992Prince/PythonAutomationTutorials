try:
    a = 100
    b = 0
    c =a / b
    print("Division is :",c)

except :
    print("Inside except block")
finally :
    print("I m finally bro")

print("*******************************************************")

try:
    a = 100
    b = 0
    c =a / b
    print("Division is :",c)

except ZeroDivisionError:
    print("Error is regarding ZeroDivisionError")
finally :
    print("I m again finally bro")


