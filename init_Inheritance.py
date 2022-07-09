# __init__ used to create/call a constructor

class Base(object):
    def __init__(self, name):
        print('Hi Madhav Mohan!\n')
        self.name = name

class Child(Base):
    def __init__(self, name):
        '''call to parent constructor'''
        Base.__init__(self, name)    # Parent constructor is called 
        print('Base is called')
        self.name = 'Maddy'

obj1 = Base('Mohan')
obj = Child('Madhav')
print(obj.name)
print(obj1.name)




        
    