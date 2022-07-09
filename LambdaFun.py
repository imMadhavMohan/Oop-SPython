# for having anonymous function we use lambda function
val = lambda val: val + 10
# print(val)
print('val = ',val(10))
print(type(val))

x = lambda a, b : a * b
print(x(5, 6))

# extract odd num from list
atom = [10,3,5,6,8]
oddNum = list(filter(lambda x: (x&1==0),atom)) # iterate for every num
print(oddNum)

# extract palindromic string
atom = ['gfg, geek','peep','sos','peek']
palidrome = list(filter(lambda x: x == (''.join(reversed(x))),atom))
print(palidrome)
