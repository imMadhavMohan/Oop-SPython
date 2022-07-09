drink = "Waters"
food = None

def check(arg):
    if drink == arg:
        print(drink)
    else :
        print(food)    
        
check('coldrink')  
check(drink)      

# Literals collections
fruits = ["apple", "mango", "orange"] #list
numbers = (1, 2, 3) #tuple
alphabets = {'a':'apple', 'b':'ball', 'c':'cat'} #dictionary
vowels = {'a', 'e', 'i' , 'o', 'u'} #set

print(fruits)
print(numbers)
print(alphabets)
print(vowels)
