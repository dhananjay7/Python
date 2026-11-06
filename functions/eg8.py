#WAF to check whether a number is even or odd

def evn_od(n):
    if(n % 2 == 0):
       return "EVEN"
    else :
        return "ODD"

print(evn_od(77))