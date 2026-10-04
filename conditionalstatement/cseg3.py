#Wap to find the greatest of 3 numbers

a = int(input("enter a : "))
b = int(input("enter b : "))
c = int(input("enter c : "))

if(a>=b and a>=c):
    print("A is the greatest")
elif(b>=a and b>=c):
    print("B is the greatest")
else:
    print("C is the greatest")