#print the multiplication table of a number n

n = int(input("enter a number : "))
i = 1
print("table for number",n,"is")
while(i <= 10):
    print(n*i)
    i+=1
print("table ends")