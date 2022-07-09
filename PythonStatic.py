# Static mainly used to represent the var that belongs to the class
# not to the obj , like CompName same for all the employees is gonna same.

# In python there is no need of static as it has by default some property

# All variables which are assigned a value in the class declaration are class
# variables. And variables that are assigned values inside methods are instance variables.
class Info:
    '''Collect emp data'''
    compName = 'GeekforGeeks'   # class variable(simulate static var)
    def __init__(self, name, age, id):
        self.name = name    # Instance var
        self.age = age
        self.id = id    
    def display(self):  # method to print the Instance variables      
        print(self.name, self.age, self.id)
        
    
if __name__ == "__main__":     # driver code
    obj = Info('Madhav Mohan', 23, 'C-71545')
    obj.display()
    print('Direct call to class var: '+Info.compName)
    print('Object reference call to var: '+obj.compName)
    
        

    
        
    