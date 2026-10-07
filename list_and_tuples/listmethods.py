#there are methods which are useful to use in lists such as :

# #list.append(4)  # adds one element at the end  

eg1 = [9,8,7]
append = eg1.append(1)
print(eg1)

#list.sort()  # sorts in ascending order
  
sorted = eg1.sort()
print(eg1)

#list.sort( reverse=True )  # sorts in descending order   

desort = eg1.sort(reverse=True)
print(eg1)

#list.reverse()  # reverses list    

rev = eg1.reverse()
print(eg1)

#list.insert( idx, el )  # insert element at index

insert = eg1.insert(0, 5)
print(eg1)

#list.remove(1) removes first occurence of the element 

rem = eg1.remove(1)
print(eg1)

#list.pop(idx) removes element at index

pop = eg1.pop(3)
print(eg1)