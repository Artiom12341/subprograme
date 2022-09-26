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

print("Cel mai mare divizor comun-",divizor_com(a,b,c))
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

print("Cel mai mic multiplu comun-",multmic_com(a,b,c))
#Valoarea maxima
def maxn(a,b,c):
    if a>b and a>c:
        max=a
    elif b>a and b>c:
        max=b
    elif c>a and c>b:
        max=c
    return max
print("Valoarea maxima-",maxn(a,b,c))
#Valoarea minima
def minn(a,b,c):
    if a<b and a<c:
        min=a
    elif b<a and b<c:
        min=b
    elif c<a and c<b:
        min=c
    return min

print("Valoarea minima-",minn(a,b,c))
#toti divizorii comuni
def div_com(a,b,c):
    div=[]
    while(True):
        for i in range(1,max(a,b,c)):
            if a%i==0 and b%i==0 and c%i==0:
                div.append(i)
        return div

print("Toti divizorii comuni-",div_com(a,b,c))
#cei mai mici trei multipli comuni
def multip3(a,b,c):
    mul=[]
    for i in range(1,4,1):
        mul.append(multmic_com(a,b,c)*i)
    return mul

print("Cei mai mici trei multipli comuni-",multip3(a,b,c))
#Numerele citite pot sa fie laturile triunghiului
def triun(a,b,c):
    m=''
    if (a+b>=c) and (c+b>=a) and (a+c>=b):
        m='DA'
        p=(a+b+c)/2
        s='Area triunghilui-',math.sqrt(p*(p-a)*(p-b)*(p-c))
        per='Perimetrul triunghilui-',a+b+c
    else:
        m='NU'
        s='area la un triunghi inexistent nu poate fi calculata'
        per='perimetru la un triunghi inexistent nu poate fi calculat'
    return m,s,per

print("Numerele citite pot sa fie laturile triunghiului-",triun(a,b,c))
#rezultatul functiei de gradul doi
def func(a,b,c):
    f=[]
    d=((b**2)-(4*a*c))
    if d>=0:
        x1=(-b-math.sqrt(d))/(2*a)
        x2=(-b+math.sqrt(d))/(2*a)
        f.append(x1)
        f.append(x2)
    elif d==0:
        x1=(-b-math.sqrt(d))/(2*a)
        f.append(x1)
    elif d<=0:
        f.append('functia nu are solutie')
    return f

print("Rezultatul functiei de gradul doi-",func(a,b,c))
