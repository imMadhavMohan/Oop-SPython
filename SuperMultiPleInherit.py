# Super keyword in multiple inheritance

class Mammal():
    # Initializing constructor
    def __init__(self):
        self.name = 'Dog'
        self.domestic = True
        self.tail = True
        self.mammals = True
        
    def isMammal(self): # if we want to use current class instance var
        if self.mammals:
          print('I\'m mammal')
            
    def isDomestic(self):
        if self.domestic:
           print('keep in house')        
            
class canSwim(Mammal):
    def __init__(self,can_Swim):            
        print(can_Swim, 'can\'t swim')        
        
class Animal(canSwim):
    def __init__(self, name):
        super().__init__(name) # Call to parent constructor        
    
obj = Animal('Dog')


        
    
    