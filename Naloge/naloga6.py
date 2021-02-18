
def datum(vrstica):
    sez = vrstica.split()
    sez = sez[0]
    sez = sez.split("/")
    sez = list(map(int, sez))
    sez.insert(0,sez[-1])
    sez.pop()
    return tuple(sez)

def ime(vrstica):
    sez=vrstica.split(" ")
    sez.pop(0)
    sez.pop(-1)
    string=" "
    return string.join(sez).strip()

def dolzina(vrstica):
    sez = vrstica.split()
    return int(sez[-1])


def podatki(vrstica):
    return (datum(vrstica), ime(vrstica), dolzina(vrstica))

def je_novejsa(s1, s2):
    datum1 = datum(s1)
    datum2 = datum(s2)
    for dat1, dat2 in zip(datum1,datum2):
        if dat1>dat2:
            return True
    return False

def najnovejsa(ime_datoteke, arhiv):
    najdat=(0,0,0)
    najvelikost=0
    for vrstica in arhiv:
        if ime(vrstica)==ime_datoteke:
            if je_novejsa(''.join(map(str,datum(vrstica))), ''.join(map(str, najdat))):
                najdat = datum(vrstica)
                najvelikost = dolzina(vrstica)
    return (najdat, ime_datoteke, najvelikost)


def datumi(ime_datoteke, arhiv):
    sez_date=[]
    for vrstica in arhiv:
        if ime(vrstica) == ime_datoteke:
            sez_date.append(datum(vrstica))
    sez_date.sort(key=lambda tup: (tup[0], tup[1], tup[2]), reverse=True)
    return sez_date
def odstrani(ime_datoteke, arhiv):
    i = 0
    while i<len(arhiv):
        if ime(arhiv[i])==ime_datoteke:
            del arhiv[i]
            i-=1
        i+=1

def skupna_dolzina(arhiv):
    zadnje_sez=[]
    skupne_dolzine=0
    for vrstica in arhiv:
        if najnovejsa(ime(vrstica), arhiv) not in zadnje_sez:
            zadnje_sez.append(najnovejsa(ime(vrstica), arhiv))
    for i in zadnje_sez:
        skupne_dolzine+=i[2]
    return skupne_dolzine




####################################### HELLO WORLD! ####################################################

import unittest
from random import shuffle


class TestObvezna(unittest.TestCase):
    def test_ime(self):
        self.assertEqual("ime_datoteke.md", ime("11/16/2020 ime_datoteke.md 314236"))
        self.assertEqual("ime datoteke s presledki.md", ime("11/6/2015 ime datoteke s presledki.md 123"))
        self.assertEqual("ime  s     presledki.md", ime("11/16/2020 ime  s     presledki.md 436"))
        self.assertEqual("ime  s     presledki.md", ime("1/6/2020     ime  s     presledki.md   0"))

    def test_dolzina(self):
        self.assertEqual(314236, dolzina("11/16/2020 ime_datoteke.md 314236"))
        self.assertEqual(123, dolzina("11/6/2015 ime datoteke s presledki.md 123"))
        self.assertEqual(436, dolzina("11/16/2020 ime  s     presledki.md 436"))
        self.assertEqual(0, dolzina("1/6/2020     ime  s     presledki.md   0"))

    def test_datum(self):
        self.assertEqual((2020, 11, 16), datum("11/16/2020 ime_datoteke.md 314236"))
        self.assertEqual((2015, 11, 6), datum("11/6/2015 ime datoteke s presledki.md 123"))
        self.assertEqual((2020, 11, 16), datum("11/16/2020 ime  s     presledki.md 436"))
        self.assertEqual((2020, 1, 6), datum("1/6/2020     ime  s     presledki.md   0"))

    def test_podatki(self):
        self.assertEqual(((2020, 11, 16), "ime_datoteke.md", 314236), podatki("11/16/2020 ime_datoteke.md 314236"))
        self.assertEqual(((2015, 11, 6), "ime datoteke s presledki.md", 123), podatki("11/6/2015 ime datoteke s presledki.md 123"))
        self.assertEqual(((2020, 11, 16), "ime  s     presledki.md", 436), podatki("11/16/2020 ime  s     presledki.md 436"))
        self.assertEqual(((2020, 1, 6), "ime  s     presledki.md", 0), podatki("1/6/2020     ime  s     presledki.md   0"))

    def test_je_novejsa(self):
        self.assertIs(True, je_novejsa("11/16/2020   i   m e 314236", "10/16/2020   i  m e 314236"))
        self.assertIs(True, je_novejsa("11/16/2020   i   m e 314236", "11/5/2020   i  m e 314236"))
        self.assertIs(True, je_novejsa("11/16/2020   i   m e 314236", "11/15/2015   i  m e 314236"))
        self.assertIs(True, je_novejsa("11/16/2020   i   m e 314236", "5/16/2020   i  m e 314236"))
        self.assertIs(True, je_novejsa("5/16/2020   i   m e 314236", "4/16/2020   i  m e 314236"))
        self.assertIs(True, je_novejsa("4/16/2020   i   m e 314236", "12/31/2018   i  m e 314236"))
        self.assertIs(True, je_novejsa("4/16/2020   i   m e 314236", "1/1/2018   i  m e 314236"))

        self.assertIs(False, je_novejsa("10/16/2020   i   m e 314236", "11/16/2020   i  m e 314236"))
        self.assertIs(False, je_novejsa("11/5/2020   i   m e 314236", "11/16/2020   i  m e 314236"))
        self.assertIs(False, je_novejsa("11/5/2020   i   m e 314236", "11/5/2020   i  m e 314236"))
        self.assertIs(False, je_novejsa("11/15/2020   i   m e 314236", "11/16/2020   i  m e 314236"))
        self.assertIs(False, je_novejsa("5/16/2015   i   m e 314236", "11/16/2020   i  m e 314236"))
        self.assertIs(False, je_novejsa("4/16/2020   i   m e 314236", "5/16/2020   i  m e 314236"))

    def test_datumi(self):
        vrstice = [
            "10/16/2020 ime dat.avi 314236",
            "10/14/2020 ime dat.avi   312353",
            "5/16/2020   ime dat.avi 21532",
            "12/31/2018   ime dat.avi 21532",
            "10/16/2020 some other.avi 314236",
            "10/18/2020 another file.avi 351352",
            "10/18/2018 another file.avi 314236",
        ]
        for i in range(10):
            shuffle(vrstice)
            self.assertEqual([(2020, 10, 16), (2020, 10, 14), (2020, 5, 16), (2018, 12, 31)], datumi("ime dat.avi", vrstice))
            self.assertEqual([(2020, 10, 16)], datumi("some other.avi", vrstice))
            self.assertEqual([], datumi("no such file.avi", vrstice))

    def test_najnovejsa(self):
        vrstice = [
            "10/16/2020 ime dat.avi 314236",
            "10/14/2020 ime dat.avi   312353",
            "5/16/2020   ime dat.avi 21532",
            "10/16/2020 some other.avi 314236",
            "10/18/2020 another file.avi 351352",
            "10/18/2018 another file.avi 314236",
        ]
        for i in range(10):
            shuffle(vrstice)
            self.assertEqual(((2020, 10, 16), "ime dat.avi", 314236), najnovejsa("ime dat.avi", vrstice))
            self.assertEqual(((2020, 10, 18), "another file.avi", 351352), najnovejsa("another file.avi", vrstice))
            self.assertEqual(((2020, 10, 16), "some other.avi", 314236), najnovejsa("some other.avi", vrstice))

    def test_odstrani(self):
        from random import shuffle

        f1 = ["10/18/2018 another file.avi 314236"]
        f2 = ["10/18/2020 ime dat.avi 314236"]
        f3 = ["10/18/2020 some other.avi 314236"]
        vrstice = 10 * f1 + 2 * f2 + f3

        self.assertIsNone(odstrani("another file.avi", vrstice[:]), "`odstrani` ne sme vračati ničesar")

        for i in range(10):
            kopija = vrstice[:]
            shuffle(kopija)
            odstrani("another file.avi", kopija)
            self.assertEqual(2 * f2 + f3, sorted(kopija))

        kopija = sorted(vrstice)
        odstrani("another file.avi", kopija)
        self.assertEqual(2 * f2 + f3, sorted(kopija))

        for i in range(10):
            kopija = vrstice[:]
            shuffle(kopija)
            odstrani("ime dat.avi", kopija)
            self.assertEqual(10 * f1 + f3, sorted(kopija))

        kopija = sorted(vrstice)
        odstrani("ime dat.avi", kopija)
        self.assertEqual(10 * f1 + f3, sorted(kopija))

        for i in range(10):
            kopija = vrstice[:]
            shuffle(kopija)
            odstrani("some other.avi", kopija)
            self.assertEqual(10 * f1 + 2 * f2, sorted(kopija))

        kopija = sorted(vrstice)
        odstrani("some other.avi", kopija)
        self.assertEqual(10 * f1 + 2 * f2, sorted(kopija))

        kopija = vrstice[:]
        odstrani("no such file.avi", kopija)
        self.assertEqual(10 * f1 + 2 * f2 + f3, sorted(kopija))


class TestDodatna(unittest.TestCase):
    def test_skupna_dolzina(self):
        vrstice = [
            "10/16/2020 ime dat.avi 1",
            "10/14/2020 ime dat.avi   2",
            "5/16/2020   ime dat.avi 4",
            "12/31/2018   ime dat.avi 8",
            "10/16/2020 some other.avi 16",
            "10/18/2020 another file.avi 32",
            "10/18/2018 another file.avi 64",
        ]
        for i in range(10):
            shuffle(vrstice)
            self.assertEqual(1 + 16 + 32, skupna_dolzina(vrstice))

        vrstice = [
            "10/14/2020 ime dat.avi   1",
            "5/16/2020   ime dat.avi 2",
            "10/16/2020 ime dat.avi 4",
            "12/31/2018   ime dat.avi 8",
            "10/16/2020 some other.avi 16",
            "10/18/2020 another file.avi 32",
            "10/18/2018 another file.avi 64",
        ]
        for i in range(10):
            shuffle(vrstice)
            self.assertEqual(4 + 16 + 32, skupna_dolzina(vrstice))


if __name__ == "__main__":
    unittest.main()
