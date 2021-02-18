# ogrevanje
"""
bobri = "12345"
globina = 2
bobri=bobri[len(bobri)-globina:][::-1]+bobri[:len(bobri)-globina]
print(bobri)

bobri = "54321"
luknje = [4, 2, 3]
for i in luknje:

    bobri=bobri[len(bobri)-i:][::-1]+bobri[:len(bobri)-i]

print(bobri)

#gulfanje :D spreminjanje seznama pred izvedbo.(verjetno ne velja)
bobri = "asdfghjk"
luknje = [4, 2, 3, 4]
for i in range(len(luknje)):
    if luknje[i]!=len(bobri):
        luknje[i]+=len(bobri)-luknje[i]

if len(luknje)%2 != 0:
    luknje.append(len(bobri))

print(luknje)
for i in luknje:

    bobri=bobri[len(bobri)-i:][::-1]+bobri[:len(bobri)-i]

print(bobri)

"""

# THE RESITEV

bobri = "bcdefghij"
luknje = [4,2,3,8,3,2,4,8]

dopolnilni_sez=[] #tukej bo genereran seznam ki bo zapolnu tako da se vrne na prvotno.
stevilo_bobrov=len(bobri)-1
for i in reversed(luknje):#to zapolnjuje seznam
    dopolnilni_sez.append(int(stevilo_bobrov))
    dopolnilni_sez.append(int(i))
    dopolnilni_sez.append(int(stevilo_bobrov))

luknje=luknje+dopolnilni_sez

print(luknje)

for i in luknje:

    bobri=bobri[len(bobri)-i:][::-1]+bobri[:len(bobri)-i]

print(bobri)

#print(dopolnilni_sez)























