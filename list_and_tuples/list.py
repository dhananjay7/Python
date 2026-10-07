#list is like an array of python it is used to store ordered collection of data 
#it is mutable , string is not , it can have same thing multiple times, and can also have diff data types 

lis = [78, 98.008, "Snow", 999]
print(type(lis))
print(len(lis))

print(lis[2])

lis[2] = "Rain"

print(lis[2])
print(lis)

#List slicing is also possible 

marks = [99, 92 ,30, 33, 44]
print(marks[1 : 3])
print(marks[-3 : -1])
# it is not possible to go right to left in slicing