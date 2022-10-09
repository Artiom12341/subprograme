from random import randint
k=[]
c=randint(100,999)
print("c=",c)
while c!=600:
    if ((c%6==0) and (c%8==0)):
        k.extend([c])
    c=randint(100,999)    
else:
    k.extend([c])
print("Rezultatul este-",k)
