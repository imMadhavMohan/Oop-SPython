# we can initialize the arg @ the time of declaration in case 
# if we haven't defined them @ the calling time

def myInfo(name, age=22):
    print('my name is',name,'and age is',age)
myInfo('Madhav') # no need to pass age

myInfo('Mohan',23) # default val override

# python allow us to change the order of arg pass
myInfo(age=25,name='Mukund')

# provide arg in different order
def simpleInt(p,r,t):
    print((p*r*t)/100)
simpleInt(t=10, r=5, p=5000)

# simpleInt(time = 12, rate=5, princ=5000) #we cant modify the parameter name