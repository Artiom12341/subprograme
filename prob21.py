a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
import math
#cel mai mare divizor comun
def divizor_com(a,b,c):
    #d=math.gcd(a,b,c)
    while(True):
        for i in range(1,max(a,b,c)+1):
            if a%i==0 and b%i==0 and c%i==0:
                d=i
        return d

print("Divizorii comuni-",divizor_com(a,b,c))
#cel mai mic multiplu comun
def multmic_com(a,b,c):
    if a>b and a>c:
        mult=a
    elif b>a and b>c:
        mult=b
    elif c>a and c>b:
        mult=c
    while (True):
        if((mult%a==0)and(mult%b==0)and(mult%c==0)):
            m=mult
            break
        mult+=1
    return m

print("Cel mai mic multiplu comun",multmic_com(a,b,c))
#Valoarea maxima
def maxn(a,b,c):
    if a>b and a>c:
        max=a
    elif b>a and b>c:
        max=b
    elif c>a and c>b:
        max=c
    return max
print("Valoarea maxima",maxn(a,b,c))
#Valoarea minima
def minn(a,b,c):
    if a<b and a<c:
        min=a
    elif b<a and b<c:
        min=b
    elif c<a and c<b:
        min=c
    return min

print("Valoarea maxima",minn(a,b,c))

