# Hybrid Inheritance
# Single level Inheritance & Multiple Inheritance
class A(object):
    def __init__(self):
        print('Parent-1')
    
class B(A):
    def __init__(self):
        super().__init__()
        print('child 1')

class C():
    def __init__(self):
        # A.__init__() only obj child class can call parent constructor
        print('child 2')

class D(A,C):
    def __init__(self):
        super().__init__()   # All parent constructors are refferred      
        print('Multiple inheritance')

obj1 = B()
obj2 = C()
obj3 = D()
