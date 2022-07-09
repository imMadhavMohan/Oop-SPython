# used to refer global var

x = 10

def outer():
    global x
    x+=9
    print(x)
    x = 5
    print(x)
    
print("Global call",x)
outer()