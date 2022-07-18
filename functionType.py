# Default function
def addd(num1, num3, num2=8): # same as c++
    return num1+num3+num2

print(addd(2,3))

def prod(*x):
    sum = 1
    for i in x:
        # print(i,end=' ')
        sum*=i
    return sum  

print(prod(2,3,4,5))


def fruits(a,c,b='accc'): # default value can be given to last arg only
    print(a,c,b)
    
fruits(a='app',c='clapp')  

# print specific passed arg only
def child(*name):
    print('Elder\'s child name: ', name[2])

child('a','b','c','d')

# var num of arguments
def prod(*x):
    sum = 1
    for i in x:
        # print(i,end=' ')
        sum*=i
    return sum      
    
print(prod(3,6,4,3,1)) 

# print specific passed arg only
def funct(**name):
    print('Elder\'s Mychild name: ', name['f2'])

funct(f1='a',f2='b',f3='c',f4='d') 

# Lambda functions
sum = lambda x,y : x+y
print(sum(4,3))

mul = lambda x,y,z: x*y*z
print(mul(2,3,4))

fname = 'Mohan'
lname = 'Madhav'

fullName = lambda x,y: print(f'fname is {x} & lname is {y}')
fullName(fname, lname)

# return lambda function
def fun(n):    # here we're dealing with 2 functions so we'll do 
    return lambda a : n*a  # returning a function

var = fun(7) # returns a lambda function
print(var(7))   



