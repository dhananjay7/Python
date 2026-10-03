#String can be used to perform some operations such as

# 1.) Concatenation

str1 = "Dhananjay"
str2 = "Tayade"
finalstr = str1 + " " + str2
print(finalstr)

# 2.) Length

str3 = "march is fooled"
print(len(str3))

# 3.) Indexing - it is used to access characters 

indexing = "Dhananjay Tayade"
print(indexing[4])

#the indexing of characters start from 0 in python always

# 4.) Slicing - Accessing parts of string using indexing
# syntax - str[starting_indx : ending_indx : step] ending indx is not included

slicing = "Python is easy"
slice = slicing[ 4 : 7 : 6 ]
print(slice)