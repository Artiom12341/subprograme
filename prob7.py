a1=int(input("a1="))
a2=int(input("a2="))
a3=int(input("a3="))
a4=int(input("a4="))
a5=int(input("a5="))
a6=int(input("a6="))
a7=int(input("a7="))
a8=int(input("a8="))
a9=int(input("a9="))
a10=int(input("a10="))
def maxim(x,y):
    
    if x>=y:
        m=x
    elif y>x:
        m=y
    else:
        m=x
    return int(m)

def minim(s,d):
    if s<d:
        mn=s
    elif d<s:
        mn=d
    else:
        mn=s
    return int(mn)

print("S=",(maxim(minim(a1,a2),maxim(a3,a4))+minim(maxim(a5,a6),minim(a7,a8))))
print("T=",(minim(a1,a2)+minim(a3,a4)+minim(a5,a6)+minim(a7,a8)+minim(a9,a10)+maxim(a1,a2)+maxim(a3,a4)+maxim(a5,a6)+maxim(a7,a8)+maxim(a9,a10)))
