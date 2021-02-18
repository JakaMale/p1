"""""
pravast_list=[1,2]
povecevalec=1
prepovedana=[]
steje=0
for i in range(1,150):
    stevilo_meja=pravast_list[i]
    for j in range(0,i+1-1):
        c=stevilo_meja+pravast_list[j]
        print(c,"  ",pravast_list[j],stevilo_meja,pravast_list,prepovedana)
        if c not in pravast_list and c not in prepovedana:
         pravast_list.append(c)
         pravast_list.sort()

        else:
            pravast_list=[x for x in pravast_list if x != c]
            prepovedana.append(c)
    povecevalec+=1

print(pravast_list,prepovedana)




def je_ulamovo(n):
    return n in (1, 2) or sum(je_ulamovo(x) and je_ulamovo(n-x) for x in range(1,(n+1)//2))==1


for i in range(1, 30):
    if je_ulamovo(i):
        print(i)


"""
import time
import numpy as np

t=time.time()

ulam=np.zeros(100001, dtype=int)
ulam[1]=ulam[2]=1

for n in range(2,100001):
    if ulam[n]==1:
        up=min(2*n,100000)
        ulam[n:up]+=ulam[:up-n]
    else:
        ulam[n]=0
print(time.time()-t)
for i in range(len(ulam)):
    if ulam[i]==1:
        print(i)



