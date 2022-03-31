"""
SignFunc(x)
1 if x positive
-1 if x is negative
[-1,3,7,6] 
product > 0
return 1
elif 
product ==0 
return 0
product <0
return -1
"""


def signfun(num):
    prod = 1
    for i in num:
        prod *= i
    if prod > 0:
        return 1
    elif prod == 0:
        return 0
    else:
        return -1
        

print(signfun([-1,3,7,6]))

