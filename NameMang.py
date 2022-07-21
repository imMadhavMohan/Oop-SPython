# Name Mangling Technique use to directly access methods and var
class A:
    def __fun1(self):
        self.__var = 'Hello'        
        print('Im private class Method ',self.__var)
        
    def fun(self):
        self.__fun1()
        print('I\'m normal function')            

obj = A()

obj._A__fun1()
print(obj._A__var)


