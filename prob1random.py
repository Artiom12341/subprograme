from random import randint
n=int(input("n="))
sp,sn=0,0
for i in range(n):
    c=randint(-50,50)
    print("Numere=",c)
    if c<0:
        sn+=c
    if c>0:
        sp+=c
print("Suma numerelor poz=",sp,"Suma numerelor neg=",sn,end='\n')