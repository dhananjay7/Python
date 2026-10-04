#Figure out a way to store 9 & 9.0 as separate values in the set.
#(You can take help of built-in data types)

set = {9,"9.0"}
print(set)
print(type(set))
print(len(set))

values = {
    (float,9.0),
    (int,9)
}

print(values)
print(type(values))
print(len(values))