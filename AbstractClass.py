from abc import ABC

class Polygon(ABC):
    def sides(self):
        pass

class Square(Polygon):
    def sides(self):
        print("4 sides")

class Pentagon(Polygon):
    def sides(self):
        print("5 sides")
   
obj = Pentagon() 
obj.sides()   

obj1 = Square()
obj1.sides()
    
        
        
        
    
