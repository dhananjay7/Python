#set is a collection of unordered data each element in set must be unique and immutable

#list and dictionary can never be stored since they are mutable
#no key value pair like dictionary
collection = {1,2,3,4,"Hello World"}
print(collection)
print(type(collection))

#duplicate entries are ignored by the set no error is given and it is unordered

marks = {90,90,90,89,89,89,"World","World"}
print(marks)
print(len(marks))
#lenght func also ignores the duplicate value  

#how to create an empty set : syntax ; set()

empty_set = set()
print(type(empty_set))