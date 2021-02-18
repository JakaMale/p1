# Tu dodajte svoje razrede
import random
import math
class Oseba:
    def __init__(self):
        self.hitrost = random.uniform(0.0, 5.0)
        self.smer = random.randint(0, 360)
        k1, k2 = risar.nakljucne_koordinate()
        self.x = k1
        self.y = k2
        self.krog = risar.krog(self.x, self.y, 3)
        self.okuzen = False
        self.bolan = False
        self.imun = False
        self.c = 0
        self.i = 0
        self.izoliran = False

    def premik(self, osebe):
        sirina = risar.maxX - 3
        visina = risar.maxY - 3
        kot = random.randint(-20, 20)
        self.smer += kot
        trenutnix, trenutniy = self.krog.x(), self.krog.y()
        if self.izoliran == False:
            if trenutnix >= sirina or trenutnix <= 3:
                self.smer += 2 * (180 - self.smer)
            elif trenutniy >= visina or trenutniy <= 3:
                self.smer += 2 * (90 - self.smer)
            for oseba in osebe:
                xo, yo = oseba.krog.x(), oseba.krog.y()
                xs, ys = self.krog.x(), self.krog.y()
                razdalja = math.sqrt(((xo - xs) ** 2) + ((yo - ys) ** 2)) - 3
                if 0 < razdalja < 20 and oseba.izoliran:
                    self.smer += 180
            rad = math.radians(90 - self.smer)
            premikx = math.cos(rad) * self.hitrost
            premiky = math.sin(rad) * self.hitrost
            risar.premakni_za(self.krog, premikx, premiky)
        else:
            self.i += 1
            if self.i == 100:
                risar.zapolni(self.krog, risar.crna)
                self.izoliran = False
                self.i = 0
            else:
                return


    def okuzi_se(self):
        if self.bolan is False and self.imun is False:
            risar.spremeni_barvo(self.krog, risar.rdeca)
            self.okuzen = True
            self.bolan = True
            nijz.sporoci_okuzbo()

    def okuzi_bliznje(self, osebe):
        for oseba in osebe:
            xo, yo = oseba.x, oseba.y
            xs, ys = self.krog.x(), self.krog.y()
            razdalja = math.sqrt(((xo - xs) ** 2) + ((yo - ys) ** 2))
            if razdalja < 3 and self is not oseba:
                oseba.okuzi_se()

    def zdravi_se(self):
        if self.bolan:
            self.c += 1
            if self.c == 150:
                risar.spremeni_barvo(self.krog, risar.zelena)
                self.imun = True
                self.bolan = False
                nijz.sporoci_ozdravitev()

    def vrni_krog(self):
        return self.krog

    def v_izolacijo(self):
        risar.zapolni(self.krog, risar.rumena)
        self.izoliran = True

    def je_izolirana(self):
        if self.izoliran:
            return True
        else: return False

import risar
class NIJZ:
    def __init__(self):
        self.stokuzb = 0
        self.stozdravelih = 0
        self.dan = 1
        self.y, self.y1 = risar.maxY, risar.maxY
    def sporoci_okuzbo(self):
        self.stokuzb += 1
    def sporoci_ozdravitev(self):
        self.stozdravelih += 1
        self.stokuzb -= 1
    def porocaj(self):
        self.dan += 1
        risar.crta(self.dan - 1, self.y, self.dan, risar.maxY - self.stokuzb, risar.rdeca)
        risar.crta(self.dan - 1, self.y1, self.dan, risar.maxY - self.stozdravelih, risar.zelena)
        self.y, self.y1 = risar.maxY - self.stokuzb, risar.maxY - self.stozdravelih

nijz = NIJZ()

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

    osebe = [Oseba() for _ in range(100)]
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


