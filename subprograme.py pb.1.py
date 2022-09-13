#liste cu int si float
a=int(input("numar de caractere="))
def listaint(n):
    lista1=[]
    for i in range(n):
        x=eval(input("Dati elementele din lista int="))
        if type(x)==int:
            lista1.append(x)
        elif type(x)!=int:
            print("Nu ati dat un numar intreg")
    return lista1
print(listaint(a))

def listafloat(c):
    lista1=[]
    for i in range(c):
        b=eval(input("Dati elementele din lista float="))
        if type(b)==float:
            lista1.append(b)
        elif type(b)!=float:
            print("Nu ati dat un numar real")
    return lista1

print(listafloat(a))
#problema cu suma
def suma():
    s=1
    for i in range(2,9,2):
        s+=0.5**i
    return print(s)

suma()

#problema cu factorial
print("n>m")
n=input("n=")
m=input("m=")
def factorial(x):
    fact=1
    for i in range(1,x+1):
        fact*=i
    return fact

c=factorial(n)/(factorial(m)*(factorial(n-m)))
print(c)

#adunarea fractiilor
# prima fractie a/b
# a doua fractie c/d
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
d=int(input("d="))
def adunare():
    x=str(input('suma sau produs? :'))                                                                  
    if x=='s' or x=='suma':     
        s=(((a*d)+(b*c))/(b*d))
        return s
    elif x=='p' or x=='produs':
        p=((a*c)/(b*d))
        return p
print(adunare())"""



