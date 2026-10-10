#Print the elements of the following list using a loop:[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
indx = 0
#traverse
while (indx < len(num)):
    print(num[indx])
    indx += 1
print("loop ends")
