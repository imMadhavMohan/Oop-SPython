# Implicit Conversion
x = 123;
y = 12.3;
z = x + y;
print(type(z), z); # float 135.3

r = "1999";
s = 9;
# z = r + s; # Give Error
# print(type(z), type(s)); error: Py cant do int & string concatenation 

print('\n');

# Explicit Conversion
p = 120;
q = "235";
print(type(p));
print(type(q));

q = int(q);
print(type(q));

r = p+q;
print(r);
print(type(r));


