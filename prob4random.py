from random import randint
n=int(input("n="))
s1=0
s0=0
for i in range(n):
    c=randint(1,6)
    print("c=",c)
for j in range(n):
    g=randint(1,6)
    print("g=",g)
    if g==c:
        s0+=2*g
    else:
        s1+=c
        s1+=g
print("Suma dublelor=",s0)
print("Suma =",s1)
