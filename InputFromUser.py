# input() from user
from traceback import print_stack


num = input('Enter your name: ')
x = input('Enter your age: ')
sal = input('Enter your salary: ')
# return input in the form of string
print('\n')

print('My age is: ',x)
print('My name is: ',num)
print('My Salary is: ',sal)

# take int input
x = int(input('Enter num1: '))
y = int(input('Enter num2: '))

# float input
f1 = float(input('Enter num1: '))
f2 = float(input('Enter num2: '))
print('sum of floats is:{} '.format(f1+f2))
# take input in list
list1 = list(input('Enter atoms in 1st list: '))
list2 = list(input('Enter atoms in 2nd list: '))

for val in list1:
   list2.append(val) 


# 1st char of string is as input
char1 = input('Enter char1: ')
print(char1[0])   # learn only 1st char

char2 = input('Enter char2: ')[0]
print(char2)   # learn only 1st char

# last char of string is as input
char3 = input('Enter char3: ')
l = len(char3)
print(char3[l-1]) # learn only n-1 char or string

print('My age is: ',x)
print('My name is: ',num)
print('My Salary is: ',sal)
print('sum is {0} & num1 is {1}'.format(x+y, x))
print('appended list is {} & {} & {}'.format(list2, list1, 12))

