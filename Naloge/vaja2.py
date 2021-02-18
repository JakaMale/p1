"""
xs = [5, 4, -7, 2, 12, -3, -4, 11, 2]

for i in xs:
    videl_sem_42=i==42
    if videl_sem_42:
        break

print(videl_sem_42)
if videl_sem_42:
    print("Res sem videl 42.")



xs = ['foo', 'bar', 'baz', 'Waldo', 'foobar']
for i in xs:
    videl_sem_waldo=i=="Waldo"
    if videl_sem_waldo:
        break

print(videl_sem_waldo)



xs = [5, 42, 4, -7, 2, 12, -3, -4, 42, 11, 2]
koliko_42=0
for i in xs:
    videl_sem_42=i==42
    if videl_sem_42:
        koliko_42+=1


print("Število 42 se v seznamu pojavi", koliko_42, "krat.")




xs = [5, 42, 4, -7, 2, 12, -3, -4, 42, 11, 2]

for i in xs:
    veckratnik=42%i==0
    if veckratnik:
        print(veckratnik)
        break
else:
    print(veckratnik)

xs = [42, 4, -7, 2, 12, -3, -4, 42, 11, 2]

for i in xs:
    veckratnik=42%i==0
    if veckratnik==False:
        print(veckratnik)
        break
else:
    print(veckratnik)



stevilo=int(input("vnesi stevilo"))

i=1
while i<=stevilo:
    if stevilo%i==0:
        print(i)
    i+=1



stevilo=int(input("vnesi stevilo"))

i=1
vsota=0
while i<=stevilo:
    if stevilo%i==0:
        vsota+=i
    i+=1

print(vsota)



stevilo=int(input("vnesi stevilo"))

i=1
vsota=0
while i<stevilo:
    if stevilo%i==0:
        vsota+=i
    i+=1
if vsota==stevilo:
    print(stevilo, "je popolno stevilo.")


#Prijateljska števila


stevilo=int(input("vnesi stevilo"))

i=1
j=1
vsota=0
vsota2=0
while i<stevilo:
    if stevilo%i==0:
        vsota+=i
    i+=1

while j<vsota:
    if vsota%j==0:
        vsota2+=j
    j+=1

if vsota2==stevilo:
    print(stevilo, "ima prijatelja")
else:
    print(stevilo, "nima prijatelja")


#Praštevilo

stevilo=int(input("vnesi stevilo"))

i=1
vsota=0
while i<=stevilo:
    if stevilo%i==0:
        vsota+=1
    i+=1

if vsota>2:
    print(stevilo,"ni prastevilo")
else:
    print(stevilo, "je prastevilo.")


#prastevila

for stevilo in range(2,100):
    i = 1
    vsota = 0
    while i<=stevilo:
        if stevilo%i==0:
            vsota+=1
        i += 1
    if vsota == 2:
        print(stevilo, "pravstevilo")

"""

#kino

filmi = [
    ('Poletje v skoljki 2', 6.1),
    ('Ne cakaj na maj', 7.3),
    ('Pod njenim oknom', 7.1),
    ('Kekec', 8.1),
    ('Poletje v skoljki', 7.2),
    ('To so gadi', 7.7),
]


"""
for naslov, ocena in filmi:
    if ocena>=7:
        print(naslov)


najvecja=0
najvecja_ocena_naslov=""
for naslov, ocena in filmi:
    if ocena>najvecja:
        najvecja=ocena
        najvecja_ocena_naslov=naslov

print(najvecja_ocena_naslov)


for naslov, ocena in filmi:
    if ocena>=7:
        print(naslov)
        break



skupaj=0
stevilo=0
for naslov, ocena in filmi:
    skupaj+=ocena
    stevilo+=1
print(round(skupaj/stevilo,2))
"""



"""
#kino 2

filmi = ['Poletje v skoljki 2', 'Ne cakaj na maj', 'Pod njenim oknom', 'Kekec', 'Poletje v skoljki', 'To so gadi']
ocene = [6.1, 7.3, 7.1, 8.1, 7.2, 7.7]


for filmi, ocene in zip(filmi, ocene):
    presledki=0
    if filmi.count(" ")==2:
        print(filmi,ocene)
"""















