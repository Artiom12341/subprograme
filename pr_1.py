a=int(input("a="))
b=int(input("b="))
from ast import Return, While
import math
#Suma numerelor
def suma(a,b):
    s=a+b
    return s

print("Suma celor doua numere=",suma(a,b))
#Produsul numerelor
def produs(a,b):
    p=a*b
    return p

print("Produsul celor doua numere=",produs(a,b))
#Media aritmetica
def medart(a,b):
    m=(a+b)/2
    return m

print("Media aritmetica celor doua numere=",medart(a,b))
#Cel mai mare divizor comun
def divizor(a,b):
    d=math.gcd(a,b)
    return d

print("Cel mai mare divizor comun=",divizor(a,b))
#Cel mai mic multiplu comun
def multipcom(a,b):
    if a>b:
        mult=a
    else:
        mult=b
    while (True):
        if((mult%a==0)and(mult%b==0)):
            m=mult
            break
        mult+=1
    return m

print("Cel mai mic multiplu comun=",multipcom(a,b))
#Numarul minim
def nummin(a,b):
    minim=min(a,b)
    return minim

print("Numarul minim=",nummin(a,b))
#Numarul maxim
def nummax(a,b):
    maxim=max(a,b)
    return maxim

print("Numarul maxim=",nummax(a,b))
#Suma numerelor citite
def sumnum():
    x=int(input("x="))
    v=int(input("v="))
    sum=x+v
    return sum

print("Suma numerelor citite=",sumnum())
#Produsul numerelor citite
def prodnum():
    x=int(input("x="))
    v=int(input("v="))    
    prod=x*v
    return prod

print("Produsul numerelor citite=",prodnum())
#Toti divizorii comuni
def divcom(a,b):
    list=[]
    for i in range(1,min(a,b)+1):
        if a%i==0 and b%i==0:
            list.append(i)
    return list

print("Divizorii comuni=",divcom(a,b))
#Cinci multipli comuni
def multimpli(a,b):
    listamult=[]
    for i in range(1,6):
        mi=a*b*i    
        listamult.append(mi)
    return listamult

print("Cinci multipli comuni=",multimpli(a,b))
#Cifrele care se contin in ambele numere
def cifcom(a,b):
    com=[]
    l2=[]
    for i in str(max(a,b)):
        l2.append(i)
    for g in str(min(a,b)):
        if g  in l2 and g not in com:
            com.append(g)
    return com

print("Cifrele care se contin in ambele numere=",cifcom(a,b))
#Cifrele care sunt in primul numar si nu sunt in al doilea
def cifdif(a,b):
    dif=[]
    l1=[]
    for i in str(b):
        l1.append(i)
    for g in str(a):
        if g  not in l1 :
            dif.append(g)
    return dif

print("Cifrele care sunt in primul numar si nu sunt in al doilea=",cifdif(a,b))
#Verificarea prietenii
def prieteni(a,b):
    lista1=[]
    lista2=[]
    for i in range(1,a+1):
        if a%i==0:
            lista1.append(i)
    for l in range(1,b+1):
        if b%l==0:
            lista2.append(l)    
    P=''
    if len(lista1)==len(lista2):
        p='PRIETENE'
    if len(lista1)!=len(lista2):
        p='NU PRIETENE'        
    return p
print("Verificarea prietenii-",prieteni(a,b))
