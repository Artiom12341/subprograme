a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
import math
def mediane(a,b,c):
    if (a+b>=c) and (c+b>=a) and (a+c>=b):
        m=0.5*math.sqrt((2*(b**2))+(2*(c**2))-(a**2))
    return m

print("lungimea medianelor-",mediane(a,b,c))