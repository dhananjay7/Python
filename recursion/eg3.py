#write a recursive function to print all the elements in a list.

def prin_lis(list , idx= 0):
    if(idx == len(list)):
        return
    print(list[idx])
    prin_lis(list , idx + 1)

fruits = ["mango","orange","banana"]

prin_lis(fruits)