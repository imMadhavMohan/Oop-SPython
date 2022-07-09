# Static methods
from os import stat
from sys import displayhook


class PersonInfo(object):
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
    
    def display(self): # Object method as instance variables are passed
        print(self.name, self.age, self.city)
    
    @staticmethod
    def isAdult(age):  # not passing the instance var
       if age >= 18 :
         print('Adult able to cast vote')   
       else :
         print('Under Age')   


if __name__ == '__main__':
    obj = PersonInfo('Madhav Mohan', 23, 'Agra')        
    obj.display()
    PersonInfo.isAdult(23)
