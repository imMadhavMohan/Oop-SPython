# Class creation
class Employee:
    # instance attributes
    comp_name = 'Luxoft India'
    def __init__(self, name, age, id):
        self.name = name
        self.id = id
        self.age = age
    def sayHi(self):
        print('Hi {}'.format(self.name))
        
    def idReturn(self):
        return self.id

# Create Object
Person = Employee('Madhav', 24, 12)    
print(Person.__class__.comp_name) # Accessing 
print(Person.name, Person.age, Person.idReturn(), Person.sayHi())
