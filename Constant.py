import Module

print(Module.Pi,'\n',Module.Gravity, Module.Epsilon);

print(Module.add(4,5));

# By the way we can reassign the constants python don't
# don't restrict this from happening

Module.Pi = 3.145;
print(Module.Pi);