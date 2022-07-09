from logging import exception


arr = ['Maddy', 23, 'Mohan', 'Agra']
for val in range(len(arr)):
    print(val, arr[val])
    
try :
    for i in range(6): # causing error out of range
        print(i, arr[i])        
except: 
    print("Handle error here")
    

val = 4
try:
   j = val/0
   print(j)
except: 
    print('Don\'t divide by zero')
        
            