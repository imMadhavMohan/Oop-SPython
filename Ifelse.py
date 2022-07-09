# if Else
val = 4;

if val > 2:
    print('more than 2');
else :
    print('less than 2');
    
# nested if else

if val > 0:
    if val > 2:
        print('more than 2');
    else : print('less than 2');
else :
    print('negative number');

# Python doesnt allow us Ternanry operator but we can 
# use if else like
def max(a, b):  
    return b if a>b else a
print(max(12,9))
  
def infoMe(a,b,c):
    print(a) if c>18 else print(b)
    
infoMe("Adult", "Adolescent",19)
    
    