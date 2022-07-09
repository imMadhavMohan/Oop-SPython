# Here when we make an obj a automatic: def __init__() gets created
class Student: # we dont want to implement this class here
    ''' Student class'''
    pass

class Employee:
    city = 'Agr' 
    comp_name = 'Luxoft, Blr'
    def __init__(self, name, age, id): # Constructor parameterized constructor
            self.name = name
            self.age = age
            self.id = id
       
    def sayHi(self):
        print('Hi {}'.format(self.name))
        
    def sayBye(abc): # Give any arg to access th obj var
        print('Bye-Bye!'+abc.name)

obj = Employee('John Doe', 23, 12)
obj.sayBye()
obj.sayHi()
print(obj.__class__.comp_name, obj.__class__.city)

del obj # delete obj