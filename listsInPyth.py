from audioop import reverse
import random
import re

# list can contain hetrogenous data
lists1 = [1,22,'Madhav Mohan','Agra']
lists2 = [1,22,'Madhav Mohan','Agra']
print(lists1 == lists2) # True

print('name & age is : %s %d',lists1[0],lists1[1])

lists3 = [1,2,3,4,5,6,7,8,9]
print(lists3[1:])
print(lists3[3:6])
print(lists3[5:9])

print(lists3[-2])
print(lists3[-7:])
print(lists3[-6:-1])

# list modify 
lists3[4] = 'A'
lists3[-4] = 'B'
print(lists3[:])

# append() in list
lists3.append([11,12,13,14])
print(lists3[:])

# concatenation
odd = [1,3,5,7,9]
odd+=[11,13,15]
print(odd)

# extend() in list
even = [2,4,6,8,10]
even.extend([12,14,16,18])
print(even)

# reverse a list
even.reverse()
print(even)

# reverse a list using slicing operator with this syntax only
revEven = even[::-1]
print(revEven)

# take an specific portion out list[start:end:step]
data = [1,2,3,4,5,6,7,8,9]
x = data[7:2:-1] # Reverse print
print(x)
x = data[7:2:-2] # Reverse print, step = -2
print(x)
x = data[2:7:2] # Reverse print, step = -2
print(x)

# Print in reverse order
even = [2,4,6,8,10,12,14]
for val in reversed(even):
    print(val,end=' ')
print('\n')    

# sort a list 
even = [2,8,4,6,12,10]
even.sort()
print(even)

# if we set reverse = True than it set descending
random.shuffle(even)
even.sort(reverse=True)
print(even)

# sort on the basis of key = customize as per user

def getName(emp):
    return emp.get('Name')

def getAge(emp):
    return emp.get('age')

def gatSal(emp):
    return emp.get('sal')

data = [
        {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
        {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
        {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
        {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},    
    ]

data.sort(key=getAge) # Ascending order
print(data)
print('\n')
data.sort(key=getAge, reverse=True) # Descending order
print(data)
print('\n')
random.shuffle(data)



