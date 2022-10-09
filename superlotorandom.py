from random import randint
def super():
    k=[]
    for g in range(5):
        k.extend([randint(1,36)])
    return k

n=1
for i in range(10):
    print("Rezultatul",n,"Superlotto 5 din 36=",super())
    n+=1