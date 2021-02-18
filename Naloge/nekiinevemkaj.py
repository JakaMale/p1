"""
def getKey(item):
    return item[0]

intervali = [tuple(int(x) for x in vrstica.split("-")) for vrstica in open("intervali.txt")]
intervali=sorted(intervali, key=getKey)

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


print(stevilo_dovoljenih)

"""


from math import sqrt
from itertools import count, islice

def is_prime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n)-1)))


sez=[2,
3,
5,
7,
13,
17,
31,
37,
43,
73,
101,
157,
197,
211,
241,
257,
307,
401,
421,
463,
577,
601,
677,
757,
1123,
1297,
1483,
1601,
1723,
2551,
2917,
2971,
3137,
3307,
3541,
3907,
4357,
4423,
4831,
5113,
5477,
5701,
6007,
6163,
6481,
7057,
8011,
8101,
8191,
8837,
9901,]

for i in sez:
    print(is_prime(i))


