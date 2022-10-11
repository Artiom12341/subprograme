from random import randint
for h in range(1):
    n=randint(2,999)
for t in range(1):
    b=randint(2,9)
for k in range(1):
    a=randint(2,999)
print("n=",n,"b=",b,"a=",a)
def baza(x,y):
    for i in [int(j) for j in str(x)]:
        if i<y:
            m= ""
        else:
            m= "nu"
            break
    return m
    
print("Numarul",n,baza(n,b),"este in baza",b)
print("Numarul",a,baza(a,b),"este in baza",b)
if ((baza(n,b)=="") and (baza(a,b)=="")):
    def transb10(x,y):
        s=0
        g=(len(str(x))-1)
        for i in str(x):
            s+=int(i)*(y**int(g))
            g-=1
        return s
    
    def b10trans(x,y):
        l=''
        c=x//y
        while c!=0:
            a=x%y
            if c>0:
                l+=str(a)
            x//=y
            c=x//y
        else:
            l+=str(x%y)
        return l[::-1]

    print("Suma numerelor date=",b10trans(transb10(n,b)+transb10(a,b),b))
    if a>n:
        print("Modulul diferentei numerelor date=",b10trans(transb10(a,b)-transb10(n,b),b))
    elif n>a:
        print("Modulul diferentei numerelor date=",b10trans(transb10(n,b)-transb10(a,b),b))
    print("Produsul numerelor date=",b10trans(transb10(n,b)*transb10(a,b),b))
else:
    print("Numerele propuse nu respecta conditia, mai incerca!")

