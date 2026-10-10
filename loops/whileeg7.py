#WAP to find the sum of the first n numbers.(using while)

n = int(input("enter a number :"))
i = 1
sum = 0
while(i <= n):
    sum = sum + i
    i+=1
print(sum)
