import time
t=time.time()
def getKey(item):
    return item[0]
import time
intervali = [tuple(int(x) for x in vrstica.split("-")) for vrstica in open("intervali.txt")]
intervali=sorted(intervali,)

stevilo_dovoljenih=0
i = 0
ni_vsebovana = 0
for spodnja, gornja in intervali:

    if spodnja == 0 or spodnja <= i or i+1 == spodnja:
        if i <gornja:
            i=gornja
    else:
        stevilo_dovoljenih+=spodnja-i-1
        i+=spodnja-i
        if spodnja == 0 or spodnja <= i or i + 1 == spodnja:
            if i < gornja:
                i = gornja

print(time.time()-t)
print(stevilo_dovoljenih)

#Drugi del se mi ne sanja. Bom razmislil.