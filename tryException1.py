num = 12
val = int(input('Enter your val: '))

try:
    rem = num/val
except ZeroDivisionError:
    print('Don\'t div by zero')  
else :  # always run when 
    print('will run')    
finally:
    print('Always run')                     
      
    
        
        
            
        


