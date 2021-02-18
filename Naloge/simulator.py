


import random
import risar
from math import cos,sin,radians,pi



class Oseba:

    def __init__(self):
        self.heading = random.randint(0,360)
        x,y= risar.nakljucne_koordinate()
        self.speed = random.uniform(0,5)
        self.r=5
        self.dni=0
        self.izolacija=0
        self.zdravje="zdrav"
        self.isolation=False
        self.krog = risar.krog(x,y,self.r, risar.bela ,)



    def premik(self, osebe):

        if risar.maxX <= self.krog.x() or self.krog.x() <= 0 :
            self.heading += (90 - self.heading)*2
        elif risar.maxY <= self.krog.y() or self.krog.y() <= 0:
            self.heading += (180 - self.heading) * 2
        for i in osebe:
            if i.isolation and (self.krog.x() - i.krog.x()) ** 2 + (self.krog.y() - i.krog.y()) ** 2 <= (20) ** 2:
                self.heading += 180

        nx, ny = self.speed * cos(radians(self.heading)), -self.speed * sin(radians(self.heading))

        if self.isolation==False:
            risar.premakni_na(self.krog,nx+self.krog.x(),ny+self.krog.y())
        else:self.izolacija+=1

        if self.izolacija==100:
            self.izolacija=0
            self.isolation=False
            risar.zapolni(self.krog,risar.crna)

    def okuzi_se(self):
        if self.zdravje=="zdrav":
            self.zdravje="bolan"
            risar.spremeni_barvo(self.krog, risar.rdeca)
            nijz.sporoci_okuzbo()


    def okuzi_bliznje(self, osebe):
        for i in osebe:
            if self != i and (self.zdravje=="bolan" or self.zdravje=="imun") and i != "bolan":
                if (self.krog.x() - i.krog.x()) ** 2 + (self.krog.y() - i.krog.y()) ** 2 <= (self.r + i.r)**2:
                    i.okuzi_se()



    def zdravi_se(self):
        if self.zdravje=="bolan":
            self.zdravje=="imun"
            self.dni+=1

        if self.zdravje== "imun":
            self.dni +=1

        if self.dni>=150 and self.zdravje=="bolan":
            self.zdravje="prebolel"
            risar.spremeni_barvo(self.krog,risar.zelena)
            nijz.sporoci_ozdravitev()

    def vrni_krog(self):
        return self.krog

    def v_izolacijo(self):
        self.isolation=True
        risar.zapolni(self.krog,risar.rumena)

    def je_izolirana(self):
        return self.isolation


class NIJZ:

    def __init__(self):
        self.st_okuzenih=0
        self.st_ozdravelih=0
        self.dan=0
        self.staray1=risar.maxY
        self.staray=risar.maxY
    def sporoci_okuzbo(self):
        self.st_okuzenih+=1
    def sporoci_ozdravitev(self):
        self.st_ozdravelih+=1
        self.st_okuzenih -=1

    def porocaj(self):
        risar.crta(self.dan,self.staray,self.dan+1,risar.maxY-self.st_okuzenih , risar.rdeca)
        risar.crta(self.dan, self.staray1, self.dan + 1, risar.maxY - self.st_ozdravelih, risar.zelena)
        self.staray = risar.maxY - self.st_okuzenih
        self.staray1 = risar.maxY - self.st_ozdravelih
        self.dan+=1


nijz = NIJZ()












# Tu dodajte svoje razrede




# Vse od tod naprej pustite pri miru

import risar

def main():
    # Tole poskrbi, da razred navidez dobi metode, ki jih še nisi sprogramiral(a)
    # Tega ni potrebno razumeti. Ignoriraj.

    from unittest.mock import Mock
    from itertools import count

    if hasattr(Oseba, "premik") and Oseba.premik.__code__.co_argcount == 1:
        Oseba.premik = lambda self, osebe, f=Oseba.premik: f(self)

    for method in ("premik", "okuzi_se", "okuzi_bliznje", "zdravi_se"):
        if not hasattr(Oseba, method):
            setattr(Oseba, method, Mock())

    globals().setdefault("nijz", None)

    osebe = [Oseba() for _ in range(1)]
    for oseba in osebe[:5]:
        oseba.okuzi_se()
    for oseba in osebe:
        if hasattr(Oseba, "vrni_krog") and hasattr(Oseba, "v_izolacijo"):
            oseba.vrni_krog().setOnClick(oseba.v_izolacijo)

    for cas in count():
        for oseba in osebe:
            oseba.zdravi_se()
            oseba.okuzi_bliznje(osebe)
            oseba.premik(osebe)
        if nijz and cas % 10 == 0:
            nijz.porocaj()
        risar.cakaj(0.02)

main()


