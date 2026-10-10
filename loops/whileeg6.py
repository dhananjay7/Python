#Search for a number x in this tuple using loop:(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input("Enter a number :"))
i = 0
while(i < len(nums)):
    if(nums[i]==x):
        print("the number is found at index",i)
    else:
        print("finding...")
    i += 1
print("loop ends")