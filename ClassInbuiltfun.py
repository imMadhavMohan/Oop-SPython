# class inbuilt function
class Student: 
    def __init__(self, name, id, age): # Parameter's passed
        self.name = name
        self.id = id
        self.age = age

obj = Student('Madhav', 12, 23)    

# print attr name of object obj
print(getattr(obj, 'name'))
print(getattr(obj, 'age'))

# reset attr
setattr(obj, 'name', 'Maddy')
print(getattr(obj, 'name'))

# check whether attr are present or not
print(hasattr(obj, 'name')) # True
print(hasattr(obj, 'city')) #False

# delattr of class
delattr(obj, 'id')

print(hasattr(obj, 'id')) # False as no more exists
# print(getattr(obj, 'id')) # Error