# Super in inheritance
# Used to call the parent class constructor & methods

class Animal():
    '''Constructor'''
    def __init__(self):
        self.name = 'DogMa'
        self.tail = True
        self.mammals = True
        self.id = 2
        self.domestic = True
        
    def isMammal(self):
        if self.mammals == True: # Accessing instance variables
            print('I\'m mammal')
    
    def isDomestic(self):
        if self.domestic == True: 
            print('safe to Keep in house')
            
class Dogs(Animal):
    def __init__(self):
        super().__init__()  
        
    def isMammal(self):          
        super().isMammal()
    
obj = Dogs()    
obj.isMammal()
obj.isDomestic()

    


        