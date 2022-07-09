# MultiLevel Inheritance

class A:
    def __init__(self):
      print("Parent Class") 
      
class B(A):
    def __init__(self):
        print("Child Class")      
        
class C(B):
    def __init__(self):     # To call any constructor we need 
        A.__init__(self)    # to explicitly call that parent constructor
        B.__init__(self)
        print("Child of child class")

obj1 = C()   
             



