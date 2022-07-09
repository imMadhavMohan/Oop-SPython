# Python program to
# demonstrate private members

# Creating a Base class


class Base:
	def __init__(self):
		self.a = "GeeksforGeeks"
		self.__c = "GeeksforGeeks"

# Creating a derived class
class Derived(Base):
	def __init__(self):
		# Calling constructor of Base class
		Base.__init__(self)
		print("Calling private member of base class: ")
		print(self.__c)


# Driver code
obj1 = Base()
print(obj1.a)

# print(obj1.c) # Error cant call private member raise an AttributeError

# obj2 = Derived() cause Error as we cant call private member in subclass

# But Using Mangling we can call Private member outside the class


class Modifiers:

    def __init__(self, name):
        self.__var = 12  # Private Attribute
        self.__var1 = name  # Private Attribute
 
print("___________Output_____________")

m = Modifiers('Maddy')

print(m._Modifiers__var)
m._Modifiers__var1 = "Github"

print(m._Modifiers__var)
print(m._Modifiers__var1)
