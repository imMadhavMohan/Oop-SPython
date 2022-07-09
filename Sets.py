# Sets stores only unique data remove duplicate element
# 1st way to create set
mySet = {1,2,'maddy',4.5,'Agra'}
print(mySet)

# 2nd way to create set
mySet1 = set([1,4.5,'Mohan','U.p'])
print(mySet1)

# creating a set having mutable data members gives error
# mySet3 = set([1,2,3,4.9,[4,3,2,1],'MadhavMohan']) # traceback error
# mySet4 = {1,2,3,4,[1,34,2,'Madhav'],3.6} # unhashable list 

# Add element to the set Using update()
mySet.update(['Noida','Delhi',2,3],{'Bgr','kta'}) #Add multiple values
print(mySet)

# Add a single element to the set
mySet.add('Jk')
mySet.add(1909)
print(mySet)
 
# Remove item from set
mySet.remove(4.5)
print(mySet)
# mySet.remove(4.5) # error as 4.5 has been removed

# Discard & remove are same only 1 difference is there
mySet.discard('Agra')
print(mySet)
mySet.discard('Agra') # no error despite 4.5 has been removed

# Set Operations
    # Union
A = set([1,2,3,4])
B = set([3,4,5,6])
print(A|B)
print(A.union(B))

    # intersection
A = set([1,2,3,4])
B = set([3,4,5,6])
print(A&B)
print(A.intersection(B))    

    # intersection_update
C = set([1,2,3,4])
D = set([3,4,5,6])
print(C.intersection_update(D))

    # difference
A = set([1,2,3,4])
B = set([3,4,5,6])
print(A-B)
print(A.difference(B)) 

    # Sort
A = set([1,4,3,5,2]) # doesnt modify the original set
print(sorted(A))

    # sum of all elements
print(sum(A))
    
# frozensets are immutable cant modify or update like set

A = frozenset([1,2,3,4])
print(A)
# A.add(5) # Error

# if we pass any dictionary to frozenset so it will only store keys
D = {'name':'madhav', 'city':'agra', 'age':'23'}
ans = frozenset(D)
print(D)
    
# To clear a set
# mySet.clear()
# print(mySet)

