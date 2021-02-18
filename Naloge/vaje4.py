
sez = [1, 2, 3, 4, 5, 6, 7, 8, 9]

class Rezalnik:
    def __init__(self,s):
        self.s = s
        self.dol = 2
    def razrezi(self,s):
        new = []
        for i in range(0, len(s), self.dol):
            new.append(s[i: i + self.dol])
        return new
    def nastavi_dolzino(self,dol):
        self.dol=dol



r= Rezalnik(sez)
r.nastavi_dolzino(3)
print(r.razrezi(sez))
import random
import risar
import math
krogi = []
while len(krogi) < 1000:
    x, y = risar.nakljucne_koordinate()
    r = random.randint(20, 80)
    for xx, yy, rr in krogi:
        dist = math.sqrt((xx - x)**2 + (yy - y)**2)
        r = min(r, dist - rr)
        if dist <= rr:
            break
    else:
        krogi.append((x, y, r))
        risar.krog(x, y, r)
risar.stoj()