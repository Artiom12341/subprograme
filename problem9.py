a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
import math
def inaltimi(a,b,c):
    l=[]
    if (a+b>=c) and (c+b>=a) and (a+c>=b):
        p=(a+b+c)/2
        na=(2*math.sqrt(p*(p-a)*(p-b)*(p-c)))/a
        nb=(2*math.sqrt(p*(p-a)*(p-b)*(p-c)))/b
        nc=(2*math.sqrt(p*(p-a)*(p-b)*(p-c)))/c
        l.append(na)
        l.append(nb)
        l.append(nc)
    return l

print("inaltimile triunghiului ABC-",inaltimi(a,b,c))