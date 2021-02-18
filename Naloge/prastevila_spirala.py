
from math import sqrt
from itertools import count, islice

def je_prime(stevilo):
    return stevilo > 1 and all(stevilo % i for i in islice(count(2), int(sqrt(stevilo)-1)))


a=1 #so robovi spirale
n=1 #pristeva da dobim nasledni rob
stevilo_primou=0
for i in count(1):

    a+=n
    if a>10000:
        break

    if je_prime(a):
        print(a)
        stevilo_primou+=1

    if i%2==0: #vsak drugi korak zanke se poveca n.
        n+=1



print(stevilo_primou)








