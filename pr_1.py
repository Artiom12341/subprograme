a=int(input("a="))
b=int(input("b="))
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
    s=0
    if a>b:
        for i in range(1,a+1):
            while a%i!=0 and b%i!=0:
                s+=1
            else:    
                break
    elif a<b:
        for i in range(1,b+1):
            while a%i!=0 and b%i!=0:
                    s+=1
            else:    
                break
    return i

print("Cel mai mare divizor comun=",divizor(a,b))