# Number datatype support: int, float, complex
print(type(5))
print(type(5.0))
print(type(5+5j))

print('\n')

print(0x15) # Ocatal to decimal 13 = pow(8,1)*1 + pow(8,0)*5
print(0b10011) #Binary to decimal conversion
print(0x15) #Hexadecimal to decimal conversion

# Typeconversion Implicit
print(type(3+4.0)) #float
print(type("maddy"+'A')) #string str

# Typeconversion Explicit
print(int(4.5))
print(float(4))
print(type(str(54)))

# Python Decimal and float
# when we want deep precision so we use Decimal instead of float
import decimal
import random
print(1/3) #less accuracy
print(decimal.Decimal(1/3)) #high accuracy


# get fraction of decimal
import fractions
print(fractions.Fraction(1.3)) 
print(fractions.Fraction('1.5')) # we can pass string
print(fractions.Fraction('1.1'))
print(fractions.Fraction(4.5))

# import math
import math
print(math.e)
print(math.sqrt(16)) 
print(math.pi)
print(math.factorial(6))
print(math.exp(1))
print(math.log10(100))

# random val generate
print(random.randrange(12,18))

x = ['a', 'b', 'c', 'd', 'e', 'f']
random.shuffle(x)
print(x)

# print random element
print(random.random())