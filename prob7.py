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
def max():
    if x>y:
        x=max
    elif y>x:
        y=max
    else:
        x=max
    return max

def min():
    if x<y:
        x=min
    elif y<x:
        y=min
    else:
        x=min
    return min

print("S=",(max(min(a1,a2),max(a3,a4))+min(max(a5,a6),min(a7,a8))))
print("T=",(min(a1,a2)+min(a3,a4)+min(a5,a6)+min(a7,a8)+min(a9,a10)+max(a1,a2)+max(a3,a4)+max(a5,a6)+max(a7,a8)+max(a9,a10)))