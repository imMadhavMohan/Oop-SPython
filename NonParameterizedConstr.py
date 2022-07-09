# Non parameterized constructor has no arg
class Student:      
    sch_name = 'APS AGRA'
    sch_id = 12
    def __init__(self):
        s_name = input('Enter student name: ')
        print(s_name)
        print(self.sch_name, self.sch_id)
        
    def sayHello(self, name):  # we cant access the 
        print('Hello ',name)
    
obj = Student()

obj.sayHello('Mohan')


    