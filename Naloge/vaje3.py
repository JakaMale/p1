"""
#1
a = input("vnesi niz")
print(len(a))

#2
l = [5, 4, -7, 2, 12, -3, -4, 11, 7]
najmajnse = max(l)
for i in l:
    if i<najmajnse and i>0:
        najmajnse=i
print(najmajnse)

#3
teze = [66, 72, 84, 68, 96, 73, 80]

while len(teze)>1:
    najvecji_i = 0
    max_teza = 0
    for i, teza in enumerate(teze):
     if teza>max_teza:
          max_teza=teza
          najvecji_i=i
    del teze[najvecji_i]
    print(teze)
#3.2
    print(sum(teze)/len(teze))
    #3.3
#4
podatki = [
    ["Ana", 55, 165],
    ["Berta", 60, 153],
]
for ime, masa, visina in podatki:
    print(ime,masa/(visina/100)**2)

#5

finska = [153, 141, 152, 160, 135]
danska = [148, 148, 148, 148, 148]
danske_tocke=0
finske_tocke=0
for i in range(len(finska)):
    if finska[i]>danska[i]:
        finske_tocke+=1
    else: danske_tocke+=1

if finske_tocke>danske_tocke:
    print("finska je zmagala")
else:print("danska je zmagala")


#6
l = [4, 5, 8, 0, 4, 1, 2, 0, 0, 0, 4, 6, 10, 0, 5, 0, 12, 1, 0,]
vsota=0

for i, l in enumerate(l):
    if l != 0:
        vsota+=l
    if l==0:
        if(vsota!=0):
            print(vsota)
            vsota=0

if vsota!=0:
    print(vsota)


#7
oklepaji = input("vnesi oklepaje")
oklepajou=0
zaklepajou=0
for i in oklepaji:
    if i == '(':
        oklepajou+=1
    if i == ')':
        zaklepajou+=1
        if zaklepajov>oklepajou:
            break
if oklepajou==zaklepajou:
    print("izraz je regularen")
else:print("izraz ni regularen")

"""

# zadnja ~˘^°ˇ˘°^˘^°ˇ~^°°ˇˇ˘˘^^˛°˛

    oklepaji = input("vneis oklepaje")
    for i, oklepaj in enumerate(oklepaji):




















