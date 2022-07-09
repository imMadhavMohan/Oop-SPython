# define more than one constructor
# we can't use two constructor no matter whether parameterized or not
# as last defined constructor is considered final

class Employee:    
    def __init__(self,name,id):
        self.id = id;
        self.name = name;
    def display (self):   
        print("ID: %d nName: %s"%(self.id,self.name))
     
emp1 = Employee("Madhav",101)
emp2 = Employee("Mohan ",102)

#accessing display() method to print employee 1 information
emp1.display();
#accessing display() method to print employee 2 information
emp2.display();
        
        
         
        
        
    
        
        