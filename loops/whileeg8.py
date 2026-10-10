#WAP to find the sum of the first n numbers.(using for)

n = int(input("Enter the desired number = "))
sum = 0
for i in range(1,n+1):
    sum = sum + i
print(sum)