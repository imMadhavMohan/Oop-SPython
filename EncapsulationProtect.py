# Python program to
# demonstrate protected members
class Base:
	def __init__(self):
		# Protected member
		self._a = 2

# Creating a derived class
class Derived(Base):
	def __init__(self):
		# Calling constructor of
		# Base class
		Base.__init__(self)
		print("Calling protected member of base class: ",
			self._a)

		# Modify the protected variable:
		self._a = 3
		print("Calling modified protected member outside class: ",
			self._a)

# WE can also call protected member outside of class as its Oops can't be compared 
# with C++ / Java

obj1 = Derived()

obj2 = Base()

print("Accessing protected member of obj1: ", obj1._a) 

print("Accessing protected member of obj2: ", obj2._a)
