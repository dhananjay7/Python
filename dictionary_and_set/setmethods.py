#there are few methods in set like other funcs 
#1.) set.add(el) it adds an element

set = {2,3,4}
set.add(88)
print(set)

#sets are mutable but the elements in it are immutable

#2.) set.remove(el) it removes an element

set.remove(2)
print(set)

#if we try to remove an element which is not present in the set it gives us an error
#3.) set.pop() it randomly popes the element

collection = {"hello","world","python","kitties"}
print(collection.pop())

#4.) set.clear() it is used to empty a set
print(len(set))
set.clear()
print(len(set))

