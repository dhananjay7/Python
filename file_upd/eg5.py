#from a file containing numbers separated by comma, print the count of even numbers

with open("numbers.txt","w") as f:
    f.write("1,2,44,55,86")

with open("numbers.txt", "r") as f:
    data = f.read()
    count = 0

    for num in data.split(","):
        if int(num) % 2 == 0:
            count += 1

print("count of even numbers is : " , count)
    

