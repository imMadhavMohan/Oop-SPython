# Change Order of calling Constructors
class A:
    def __init__(self,name):
        self.name = name
        print(name)
    def print_name(self):
        print(self.name)

class B(A):
    def __init__(self,name):
        '''Call Current class constructor'''
        self.name = name
        # call parent class after child
        A.__init__(self,name)

obj = B('Madhav')         


        



  