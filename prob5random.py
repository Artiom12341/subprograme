from random import randint
k=[]
s=0
n=int(input("n="))
for i in range(n):
    k.extend([randint(1,100)])
print("k=",k)
for i in k:
    if i<max(k):
        s+=i
print("Suma =",s)