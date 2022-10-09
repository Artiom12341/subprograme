from random import randint
n=int(input("n="))
s=0
for i in range(n):
    c=randint(1,6)
    print("Valoarea de pe zar =",c)
    if c==6:
        s+=1
print("Valoarea 6 de pe zar a cazut de",s,"ori")