# Sem pišite svoje funkcije
def se_napadata(top1, top2):
    if top2==top1:
        return False
    if top2[0]==top1[0] or top2[1]==top1[1]:
        return True
def napadeni(top, topovi):
    new_sez=[]
    for i in topovi:
            if i[0] == top[0] or i[1] == top[1]:
                new_sez.append(i)
    new_sez.remove(top)
    return new_sez


def napadenost(top, topovi):
    st_napadov=0
    for i in topovi:
        if top==i:
            st_napadov-=1
        if i[0] == top[0] or i[1] == top[1]:
            st_napadov+=1

    return st_napadov

def varen(top, topovi):
    for i in topovi:
        if i[0] == top[0] or i[1] == top[1] and top!=i:
            return False
    return True

def najbolj_napaden(topovi):
    if not topovi:
        return None
    naj_top_num=0
    trenutni_top=0
    naj_top_cor=""
    for a in topovi:
        trenutni_top = 0
        for b in topovi:
            if a[0] == b[0] or a[1] == b[1] and b != a:
               trenutni_top+=1
               if naj_top_num< trenutni_top:
                   naj_top_num=trenutni_top
                   naj_top_cor=a
    if naj_top_num!=1:
        return naj_top_cor
def vse_varno(topovi):
    stevec=0
    for a in topovi:
        for b in topovi:
            if a[0] == b[0] or a[1] == b[1] and b != a:
                stevec+=1
                if stevec>1:
                    return False
    return True
def vse_varno(topovi):
    for a in topovi:
        stevec = 0
        for b in topovi:
            if a[0] == b[0] or a[1] == b[1] and b != a:
                stevec+=1
                if stevec>1:
                    return False
    return True
###!DODATNA
def direkten_napad(top1, top2, topovi):
    if top1 == top2:
        return False
    for i in topovi:
        if top1[0] == top2[0]:
            if top1[0]==i[0] and top1!=i and top2 != i:
                if int(top1[1])>int(i[1])>int(top2[1]) or int(top1[1])<int(i[1])<int(top2[1]):
                    return False

        elif top1[1] == top2[1]:
            if top1[1]==i[1] and top1!=i and top2 != i:
                if ord(top1[0])>ord(i[0])>ord(top2[0]) or ord(top1[0]) < ord(i[0]) < ord(top2[0]):
                    return False
        else:return False

    return True

import unittest


class TestObvezna(unittest.TestCase):
    def test_se_napadate(self):
        self.assertTrue(se_napadata("a4", "d4"))
        self.assertTrue(se_napadata("e8", "c8"))
        self.assertTrue(se_napadata("e8", "e5"))
        self.assertTrue(se_napadata("f4", "f6"))

        self.assertFalse(se_napadata("f4", "g8"))
        self.assertFalse(se_napadata("g8", "f4"))
        self.assertFalse(se_napadata("c3", "c3"))

    def test_napadeni(self):
        self.assertEqual(["c1", "c8", "c6", "a3", "h3"],
                         napadeni("c3", ["c1", "c3", "d6", "c8", "c6", "e5", "a3", "h3"]))
        self.assertEqual(["c1", "c8", "c6", "a3", "h3"],
                         napadeni("c3", ["c1", "c3", "c8", "c6", "a3", "h3"]))
        self.assertEqual(["c3", "c4", "c5", "a1"],
                         napadeni("c1", ["c1", "c3", "c4", "c5", "a1"]))
        self.assertEqual([], napadeni("a8", ["c1", "a8", "c6", "h3"]))
        self.assertEqual([], napadeni("a8", ["a8"]))

    def test_napadenost(self):
        self.assertEqual(5, napadenost("c3", ["c1", "c3", "d6", "c8", "c6", "e5", "a3", "h3"]))
        self.assertEqual(5, napadenost("c3", ["c1", "c3", "c8", "c6", "a3", "h3"]))
        self.assertEqual(0, napadenost("a8", ["c1", "a8", "c6", "h3"]))
        self.assertEqual(0, napadenost("a8", ["a8"]))

    def test_varen(self):
        self.assertFalse(varen("c3", ["c1", "d6", "c8", "c6", "e5", "a3", "h3"]))
        self.assertFalse(varen("c3", ["c1", "c8", "c6", "a3", "h3"]))
        self.assertTrue(varen("a8", ["c1", "c6", "h3"]))
        self.assertTrue(varen("a8", []))

    def test_najbolj_napaden(self):
        self.assertEqual("c5", najbolj_napaden(["a5", "c5", "f5", "c6", "c8", "d3", "f7"]))
        self.assertEqual("f5", najbolj_napaden(["a5", "e5", "f5", "c6", "c8", "d3", "f7"]))

        self.assertIsNone(najbolj_napaden(["a5", "c6", "e8", "d3"]))
        self.assertIsNone(najbolj_napaden([]))

        self.assertEqual("a5", najbolj_napaden(["a5", "a6"]))
        self.assertEqual("a6", najbolj_napaden(["a6", "a5"]))

    def test_vse_varno(self):
        self.assertFalse(vse_varno(["a5", "c5", "f5", "c6", "c8", "d3", "f7"]))
        self.assertTrue(vse_varno(["a5", "c6", "e8", "d3"]))
        self.assertTrue(vse_varno(["a5", "c6", "e8", "d3"]))


class TestDodatna(unittest.TestCase):
    def test_direkten_napad(self):
        pozicija = ["a5", "c5", "f5", "c6", "c8", "d3", "f7"]

        self.assertFalse(direkten_napad("a5", "a5", pozicija))

        self.assertFalse(direkten_napad("a5", "c8", pozicija))
        self.assertFalse(direkten_napad("c8", "a5", pozicija))
        self.assertTrue(direkten_napad("f5", "f7", pozicija))
        self.assertTrue(direkten_napad("f7", "f5", pozicija))

        self.assertTrue(direkten_napad("a5", "c5", pozicija))
        self.assertTrue(direkten_napad("c5", "a5", pozicija))
        self.assertTrue(direkten_napad("c5", "f5", pozicija))
        self.assertTrue(direkten_napad("f5", "c5", pozicija))
        self.assertFalse(direkten_napad("f5", "a5", pozicija))
        self.assertFalse(direkten_napad("a5", "f5", pozicija))

        self.assertTrue(direkten_napad("c5", "c6", pozicija))
        self.assertTrue(direkten_napad("c6", "c5", pozicija))
        self.assertTrue(direkten_napad("c6", "c8", pozicija))
        self.assertTrue(direkten_napad("c8", "c6", pozicija))
        self.assertFalse(direkten_napad("c8", "c5", pozicija))
        self.assertFalse(direkten_napad("c5", "c8", pozicija))
        self.assertFalse(direkten_napad("c5", "c8", pozicija))


if __name__ == "__main__":
    unittest.main()
