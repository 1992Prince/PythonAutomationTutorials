class Human:
    # below are class variables
    eyes = "blue"
    nose = "Large"

    def eyes_fun(self,color):
        print("This is function to see :",color)

    def noes_fun(self,size):
        print("This is function to smell and its size is :",size)

    def ear_fun(self,color):
        print("This is function to hear and its color is :",color)


# printing class variables without creating object of class
print("Class Var eyes :",Human.eyes," ",Human.nose)

# creating object of class and calling methods of class
# without object we can't access class methods
a = Human()
a.ear_fun("brown")
a.ear_fun("big")
a.noes_fun("black")
