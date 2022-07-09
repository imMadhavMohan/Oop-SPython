# Tuples aren't modifiable like lists
data = ('maddy', 22, 'Agr') 
print(data)
# data[0] = 'Mohan' Error
print(data)

# Tuple's cration
info = (input('input val: '))
print('output val: ',info)

# Tuple's containing lists & Tuple
info = (1,[2,3,4],(6,7,8),'maddy')
print(info)
info[1][1] = 9
# info.append(76) error message
# info.pop(4) error message
# info.clear() error msg
# info.extend((4,3,5)) error message
info = info*2
print(info) # duplicity
print(info[1])
print(info[1][2])

info += info;
print(info)


# We cant modify the Tuple, we cant use pop, remove, copy, append, extend etc
# but we can delete a tuple
del info
print(info)