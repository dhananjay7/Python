#if-elif-else is used to justify a condition 
"""
#syntax
if(condition):
    statement
elif(condition):
    statement
else:
statement
"""
#eg 1 
age = 9

if(age>=18):
    print("can vote")
    print("can drive")
else :
    print("ja jake padh le bachiii")

#eg 2
signal_color = "red" 

if(signal_color == 'red'):
    print("stop")
elif(signal_color == 'green'):
    print("go")
elif(signal_color == 'yellow'):
    print("slowdown")
else : 
    print("g mara le")

#very important point to be noted is that all these spaces we use in if else or anywhere is called indentation bcus in c++ and java we use { block of code } to compact everything but in python there is no such thing as that so we use indentation