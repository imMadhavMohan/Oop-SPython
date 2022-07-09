# these are niether local nor global they just refer uppercope variables
# changes val permanently

def outer():
    x = 'Hi'
    def inner():
        nonlocal x
        x += "Hello"
        print(x)
        x = 'Bye'
        print(x)
    inner()
    print(x)

outer()
