#WAF to find the factorial of n (n is the parameter)

def fac(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


print(fac(0))