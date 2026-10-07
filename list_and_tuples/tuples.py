# a tuple is a built in data type that is immutable and lets us create a sequence of values

tuple = (2,1,3,1)
print(tuple)
print(type(tuple))
print(len(tuple)) 

# just like list tuple can also be indexed but not mutated

print(tuple[0]) 
print(tuple[2])

# for single value always use (1 ,)comma to define a tuple 

tup = (1 ,)
print(tup)
print(type(tup))

#slicing is also allowed 

print(tuple[1 : 3])