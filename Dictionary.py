# Dictionaries are unordered data structure
# here we acess val using key
# Ways to create a dictionary
from poplib import HAVE_SSL


D1 = dict({'Name': 'Mukund',2:'B','city':'Hyd','list':[1,2,3,4]})
print(D1.keys())
print(D1.values())
print(type(D1))

D = {'Name':'Madhav', 1:'A','city':'Agra'}
print(D)

for val in D:
    print(val,end=' ')
print('\n')    
for key in D.keys():    
    print(key,end=' ')

# Access the dictionary elements
print(D['city'])
print(D.get('Name'))
print(D1.get(2))

print(D1['list'])
print(D.get('state')); # None
# print(D['state'])  # Error well get

# Get keys & values from dictionary
print(D.values())
print(D.keys())

# Add/Update dictionary element
D['city'] = 'Bgr'
D['addr'] = 'Dayal Bagh'
print(D.keys()) 
print(D.values())

# Update dictionary element
D.update({'city':'Agra'})
print(D.values())

  