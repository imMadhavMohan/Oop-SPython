# WhileLoop

from tkinter import N


n = 10
sum = 0
# sum of n numbers

while n >= 0 :
   sum+=n
   n-=1

print(sum) 

# while else loop // run when all iterations are finished
n = 5
while n >= 0 :
    print(n, "is greater than 0")
    n -= 1
else :
    print(n, "is lesser than 0")
