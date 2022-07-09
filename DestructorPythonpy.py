# Destructor is opposite to the constructor Used to destruct the constructor,
# destructor is run in the end of the class when all its referrences are destroyed

class Info:
    def __init__(self, name, id, city):
       self.name = name
       self.id = id
       self.city = city
    
    def display(self):
        print(self.name, self.id, self.city)
    
    def __del__(self): # Calling constructor
        print('Dstructor is called')

obj = Info('Madhav', 'c-1234', 'Agra') # Object Create
obj.display() 
del obj      # Object Deleted


 