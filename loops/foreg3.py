#Search for a number x in this tuple using loop:(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = int(input("enter the number : "))
idx = 0
for el in tup:
    if(el == x):
        print("element found at index :", idx)
        break
    idx += 1
else : 
    print("element not found")