def preberi_vrstice(ime_datoteke):
    datoteka=open(ime_datoteke, encoding="UTF-8")
    a=[]
    for i in datoteka:
       a.append(i.strip())
    return a
def preberi_csv(ime_datoteke):
    a=preberi_vrstice(ime_datoteke)
    b=[]
    for i in a:
        a=i.split(";")
        a[2]=float(a[2])
        a=tuple(a)
        b.append(a)
    return b
def oblikuj(podatki):
    b=[]
    for kraj,vreme,temp in podatki:
        f=f"Kraj: {kraj}, Vreme: {vreme}, Temperatura: {temp}°C"
        b.append(f)
    return b

def oblikuj_tabelo(podatki):
    b=['Kraj            Vreme           Temperatura (°C)',
       '------------------------------------------------',]
    for kraj,vreme,temp in podatki:
        b.append(f"{kraj:16}{vreme:28}{temp:4}")
    return b
def oblikuj_tabelo_f(podatki):
    b=['Kraj            Vreme           Temperatura (°F)',
       '------------------------------------------------',]
    for kraj,vreme,temp in podatki:
        temp=(temp / 5 * 9)+32
        a=f"{temp:3.1f}"
        b.append(f"{kraj:16}{vreme:28}{a:4}")

    return b
def oblikuj_pike(podatki):
    b=['Kraj            Vreme           Temperatura (°F)',
       '------------------------------------------------',]
    for kraj,vreme,temp in podatki:
        temp=(temp / 5 * 9)+32
        a=f"{temp:3.1f}"
        b.append(f"{kraj:.<16}{vreme:.<28}{a:4}")

    return b
def oblikuj_fc(podatki):
    b=['Kraj            Vreme        Temperatura °F (°C)',
       '------------------------------------------------',]
    for kraj,vreme,temp in podatki:
        c=temp
        stevilke=f""
        tem=(temp / 5 * 9)+32
        a=f"{tem:3.1f}"
        stevilke = f"{a} ({c})"
        b.append(f"{kraj:.<16}{vreme:.<15}{stevilke:.>17}")

    return b

def shrani(vrstice, ime_datoteke):
    datoteka=open(ime_datoteke, "w")
    for i in vrstice:
        i+="\n"
        datoteka.write(i)
    datoteka.close()

def najdaljse_besede(s):
    s=s.split()

    a=""
    maxi_len=0
    for i in s:
        if len(i)>=maxi_len:
            maxi_len=len(i)
    for i in s:
        if len(i)==maxi_len:
            i +=", "
            a += i

    return a[:-2]



### ^^^ Naloge rešujte nad tem komentarjem. ^^^ ###

import unittest

class Testi(unittest.TestCase):

    def setUp(self):
        f = open("podatki.txt","w",encoding='utf-8')
        f.write("Ljubljana;oblačno;12.1\n")
        f.write("Maribor;sončno;9\n")
        f.write("Koper;sončno;14.7\n")
        f.close()

        self.podatki = [('Ljubljana', 'oblačno', 12.1), ('Maribor', 'sončno', 9.0), ('Koper', 'sončno', 14.7)]

    def test_preberi_vrstice(self):
        self.assertEqual(preberi_vrstice("podatki.txt"), ["Ljubljana;oblačno;12.1", "Maribor;sončno;9", "Koper;sončno;14.7"])

    def test_preberi_csv(self):
        self.assertEqual(preberi_csv("podatki.txt"), [('Ljubljana', 'oblačno', 12.1), ('Maribor', 'sončno', 9.0), ('Koper', 'sončno', 14.7)])

    def test_oblikuj(self):
        self.assertEqual(oblikuj(self.podatki),
                         ['Kraj: Ljubljana, Vreme: oblačno, Temperatura: 12.1°C',
                          'Kraj: Maribor, Vreme: sončno, Temperatura: 9.0°C',
                          'Kraj: Koper, Vreme: sončno, Temperatura: 14.7°C'])

    def test_oblikuj_tabelo(self):
        self.assertEqual(oblikuj_tabelo(self.podatki),
                         ['Kraj            Vreme           Temperatura (°C)',
                          '------------------------------------------------',
                          'Ljubljana       oblačno                     12.1',
                          'Maribor         sončno                       9.0',
                          'Koper           sončno                      14.7'])

    def test_oblikuj_tabelo_f(self):
        self.assertEqual(oblikuj_tabelo_f(self.podatki),
                         ['Kraj            Vreme           Temperatura (°F)',
                          '------------------------------------------------',
                          'Ljubljana       oblačno                     53.8',
                          'Maribor         sončno                      48.2',
                          'Koper           sončno                      58.5'])

    def test_oblikuj_pike(self):
        self.assertEqual(oblikuj_pike(self.podatki),
                         ['Kraj            Vreme           Temperatura (°F)',
                          '------------------------------------------------',
                          'Ljubljana.......oblačno.....................53.8',
                          'Maribor.........sončno......................48.2',
                          'Koper...........sončno......................58.5'])

    def test_oblikuj_fc(self):
        self.assertEqual(oblikuj_fc(self.podatki),
                         ['Kraj            Vreme        Temperatura °F (°C)',
                          '------------------------------------------------',
                          'Ljubljana.......oblačno..............53.8 (12.1)',
                          'Maribor.........sončno................48.2 (9.0)',
                          'Koper...........sončno...............58.5 (14.7)'])

    def test_shrani(self):
        lines = ['prva vrstica', 'druga vrstica', 'tretja vrstica']
        shrani(lines, 'datoteka.txt')
        f = open("datoteka.txt", "r")
        lines_f = f.read().splitlines()
        f.close()
        self.assertEqual(lines_f, lines)

    def test_najdaljse_besede(self):
        self.assertEqual(najdaljse_besede('ob znaku bo ura deset in pet minut'), 'znaku, deset, minut')

if __name__ == '__main__':
    unittest.main(verbosity=2)
