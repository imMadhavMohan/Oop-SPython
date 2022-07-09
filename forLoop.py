# for loop
arr = [2,0,4,6,8,10,12];
for val in arr:
  print(val,sep=' ',end=' ')  
  
str = "Madhav Mohan"  
for i in str:  
  print(i,end='')   
    
print('\n')
    
    
# range() function
  # type-1
for i in range(10):
    print(i,end=' ')
print()    
    # type-2
for i in range(0,2): # start , end
    for j in range(0,2):
        print('{}{}',i,j,end=' ')
    print()
    # type-3
name = ['Ma','Mu','Js','Rm'] # obj can be consider as int
for val in range(len(name)): # will print length
    print(name[val],end=' ')
print()


# for-else 
for val in arr:
    if val == 14:
       print('found') 
       break # if found so else won't run  
else:        # will run only iterations are overed
    print('not found')    