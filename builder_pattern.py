# Design Leopard Class
class Leopard:
    # Intilaize the constructor with all the required fileds
    def __init__(self,colour,name,gender):
        self.name = name
        self.gender = gender 
        self.colour = colour

# Creating an instance of Leopard class        
l = Leopard("yellow","leopard_1","male")

# Issues with the above code

# 1. We have to remember the ordering of variables in the constructor
# 2. Suppose if we add new variable in the future previous code will not work. Code is not backward compatible.

# One idea to resolve the 1st issue is we can use setter and getters for each variable. But we know the colour of the 
# Leopard or gender of the Leopard is same till the Leopard dies. So if we use setter we are giving access to client 
# to change the colour of Leopard which is not good code.

# By modifying the above idea a little bit what we can do is create one more class and allow setter and getter in new 
# class and send that object to Leopard class. Lets see the implementation.

# In Python, we denote private attribute using underscore as prefix i.e single “ _ “ or double “ __“.

class Leopard:
    def __init__(self,obj):
        self.name = obj.get_name()
        self.colour = obj.get_colour()
        self.gender = obj.get_gender()        

class X:
    def __init__(self):
        self.__name = None
        self.__colour = None
        self.__gender = None
    # We are using setter and getters to access the variables       
    def set_colour(self,colour):
        self.__colour = colour
        return self
    def get_colour(self):
        return self.__colour
    def set_name(self,name):
        self.__name = name
        return self
    def get_name(self):
        return self.__name
    def set_gender(self,gender):
        self.__gender = gender
        return self
    def get_gender(self):
        return self.__gender
x = X()
x.set_colour("yellow")
x.set_name("leopard_1")
x.set_gender("male")
l = Leopard(x)

# Combining all the above lines to one line

x = X().set_colour("yellow").set_name("leopard_1").set_gender("male")
l = Leopard(x)

# Small change in the code to look good

class X:
    def __init__(self):
        self.__name = None
        self.__colour = None
        self.__gender = None
    # We are using setter and getters to access the variables       
    def set_colour(self,colour):
        self.__colour = colour
        return self
    def get_colour(self):
        return self.__colour
    def set_name(self,name):
        self.__name = name
        return self
    def get_name(self):
        return self.__name
    def set_gender(self,gender):
        self.__gender = gender
        return self
    def get_gender(self):
        return self.__gender
    def leopard_func(self):
        l = Leopard(self)
        return l
l = X().set_colour("yellow").set_name("leopard_1").set_gender("male").leopard_func()

# So we are using class X to create object for Leopard class. So we can rename class X as Builder class and leopard_func
# as build function. 

# One more important thing is we are enforcing client to create object of Builder class which is not good so we make 
# our Builder class as our Inner Class.

class Leopard:
    def __init__(self,obj):
        self.name = obj.get_name()
        self.colour = obj.get_colour()
        self.gender = obj.get_gender()   

    class Builder:
        def __init__(self):
            self.__name = None
            self.__colour = None
            self.__gender = None
        # We are using setter and getters to access the variables       
        def set_colour(self,colour):
            self.__colour = colour
            return self
        def get_colour(self):
            return self.__colour
        def set_name(self,name):
            self.__name = name
            return self
        def get_name(self):
            return self.__name
        def set_gender(self,gender):
            self.__gender = gender
            return self
        def get_gender(self):
            return self.__gender
        def build(self):
            l = Leopard(self)
            return l    

l = Leopard.Builder().set_colour("yellow").set_name("leopard_1").set_gender("male").build()        

print(l.name,l.colour,l.gender)

# Yayyy finally we created builder design pattern.