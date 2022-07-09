# Call Parent Method
class A(object):
    def __init__(self, name):
        print('Mame is: ',name)
    def display(self, id):
        print(id)

class B(A):    
    pass    

obj = A('Madhav')
obj.display(12)

obj1 = B('Mohan')
obj1.display(13)


        
