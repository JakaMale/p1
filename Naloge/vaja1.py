# naloga 1
"""""
skupaj=0
stevec=0
while stevec<5:
    cena=float(input("Cena artikla:"))
    skupaj+=cena
    stevec+=1
print("skupaj:", skupaj)

#naloga 2
skupaj=0
stevec=0
x=int(input("koliko artiklov je v kosarici."))
while stevec<x:
    cena=float(input("Cena artikla:"))
    skupaj+=cena
    stevec+=1
print("skupaj:", skupaj)

#naloga 3

skupaj=0
stevec=0
while True:
    cena=float(input("Cena artikla:"))
    if cena==0:
        break
    skupaj+=cena
    stevec+=1
print("skupaj:", skupaj)

#naloga 4

skupaj=0
stevec=0
while True:
    cena=float(input("Cena artikla:"))
    if cena==0:
        break
    skupaj+=cena
    stevec+=1

print("skupaj:", skupaj)
print("povprečna cena:",skupaj/stevec)

#nalga 5

skupaj=0

while True:
    cena=float(input("sprememba:"))
    skupaj += cena
    print("stanje:", skupaj)
    if skupaj<-100:
        break
        print("bankrot")
"""""

#naloga 6 (vnaša cene in ki se neha izvajati, ko uporabnik vnese 0 (ne bo več kupoval), ko je vnešenih deset števil ali ko vsota cen doseže ali preseže 100 evrov.)

skupaj=0
stevec=0
while True:
    cena=float(input("Cena artikla:"))
    skupaj += cena
    if cena!=0:
        stevec+=1

    if cena==0:
        break
    elif skupaj>100:
        break
    elif stevec==10:
        break

print("skupaj boste dali :", skupaj, "e za",stevec,"stvari")



















