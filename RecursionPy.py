# Recursion
def sumOfnum(n):
    if n<0: return 0
    else: return n+sumOfnum(n-1)

print(sumOfnum(100))

def printNum(num):
    if num<0:
        return
    print(num,end=' ')    
    num -=1
    printNum(num)

printNum(5)

def factorial(n) :
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(6))

def gcd(a,b): # T(n) = O(min(a,b))
    if(a==0):
        return b
    if(b==0) :
        return a
    
    if(a>b):
      return gcd(a-b,b)
    else:
      return gcd(a,b-a)
        
print(gcd(15,6))   

def gcd1(a,b):
    return b if a==0 else gcd(a%b,b)
print(gcd(15,31))















