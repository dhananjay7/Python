#default parameter 

def calcprod(a,b=3):  #it is the value we put in para meter in function definition so that even if we dont pass argu the code does not throw error and also it can be (a , b = 1) only if we pass argu for a in function call it only works this way not the opposite
    print(a * b)
    return a * b

calcprod(3)
