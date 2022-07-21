# yield keyword

# generator to print even numbers
def print_even(test_list):
	for i in test_list:
		if i % 2 == 0:
			yield i

# list
test = [1, 4, 5, 6, 10]

# printing even numbers
for j in print_even(test):
	print(j, end=" ")

# counting till 50
def cntNum():
    num = 0  
    while True:  
        yield num
        num+=1
    
for val in cntNum():
    if(val>50):
        break
    print(val,end=' ')

# findSquare til num 10
def nextSquare():
	i = 1
	while True:
		yield i*i		
		i += 1
		
# Driver Code
for num in nextSquare():
	if num > 100:
		break
	print(num)
