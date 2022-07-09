# Single level Inheritance 
class Animal:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def display(self):
        print(self.name, self.id)

class Dog(Animal):
    def Bark(name):
        print('dog is barking!')
                
dog = Dog('Tommy',12)        
dog.display()
dog.Bark()