# Hierarchial Inheritance
# super().__init__() == A.__init__()

class A(object):
    def __init__(self):
        print('Parent-1')
    
class B(A):
    def __init__(self):
        super().__init__()
        print('child 1')

class C(A):
    def __init__(self):
        super().__init__()
        print('child 2')

obj1 = B()
obj2 = C()
