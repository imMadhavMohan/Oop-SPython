# Parameterized constructor
class Employee:
    comp_name = 'Luxoft india'   
    location = 'Agra'
    def __init__(self, fname, lname, age):
        '''parameterized constructor'''
        self.age = age
        self.fname = fname
        self.lname = lname
    def myInfo(self):
        print(self.fname, self.lname)
    def myAge(self):
        print(self.age)

obj = Employee('Madhav', 'Mohan',23)
obj.myInfo()
obj.myAge()

    
    
        