# *args
# use for variable length non keyword arg on which tuple operation can be done
def function(*args): # 8args
    sum = 0
    for i in args:
        sum+=i
    return sum
            
print(function(2,4,5,3,6))            


# **kwarg
# use for variable length keyword arg on which dictionary operation can be done
def data(**info): 
    print(type(info))
    for key,val in info.items():
        print('{}:{}'.format(key,val))
    
data(fname='Raman',lname='Mohan',age=23,id=12)