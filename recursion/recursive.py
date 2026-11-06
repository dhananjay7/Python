# recursive functions example : print n to 1 backwards

def show(n):
    if(n == 0): #base case
        return
    show(n - 1)
    print(n)
    
show(5)

# base case is used to stop a recursive infinite loop and stop the recursive error 