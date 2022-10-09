from random import randint
s0,s1,s2,s3,s4,s5,s6,s7,s8,s9=0,0,0,0,0,0,0,0,0,0
for i in range(1):
    c=randint(1,999999999)
    print("c=",c)
    for g in str(c):
        if int(g)==0:
            s0+=1
        if int(g)==1:
            s1+=1
        if int(g)==2:
            s2+=1
        if int(g)==3:
            s3+=1
        if int(g)==4:
            s4+=1
        if int(g)==5:
            s5+=1
        if int(g)==6:
            s6+=1
        if int(g)==7:
            s7+=1
        if int(g)==8:
            s8+=1
        if int(g)==9:
            s9+=1
print("Numarul 0 a cazut de ",s0,"ori.")
print("Numarul 1 a cazut de ",s1,"ori.") 
print("Numarul 2 a cazut de ",s2,"ori.") 
print("Numarul 3 a cazut de ",s3,"ori.") 
print("Numarul 4 a cazut de ",s4,"ori.")
print("Numarul 5 a cazut de ",s5,"ori.")
print("Numarul 6 a cazut de ",s6,"ori.")
print("Numarul 7 a cazut de ",s7,"ori.")
print("Numarul 8 a cazut de ",s8,"ori.")
print("Numarul 9 a cazut de ",s9,"ori.") 
 