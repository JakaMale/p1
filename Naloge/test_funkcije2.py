def najdaljsa(s):
    sez=s.split()
    return max(sez, key=len)

def podobnost(s1, s2):
    skupaj=0
    for a, b in zip(s1,s2):
        if a==b:
            skupaj+=1
    return skupaj


def sumljive(s):
    new_sez=[]
    s=s.split()
    for i in s:
        if 'a' in i and 'u' in i:
            new_sez.append(i)
    return new_sez

def vsi(xs):
    return all(xs)

def vsaj_eden(xs):
    return any(xs)
def mrange(start, faktor, dolzina):
    sez=[]
    x=start
    for i in range(dolzina):
        sez.append(x)
        x*=faktor
    return sez


def vsota_seznamov(s):
    new_s=[]
    for i in s:
        new_s.append(sum(i))
    return new_s

def najvecji_podseznam(xs):
    new_s=[0]
    for i in xs:
        if sum(i)>sum(new_s):
            new_s=i
    return new_s

def drugi_najvecji(xs):
    res=1
    naj=max(xs)
    for i in xs:
        if i<naj and i>res:
            res=i

    return res

def cezar(xs):
    for i in range(len(xs)):
        xs[i]=chr(ord(xs[i])+3)
    return xs
### ^^^ Naloge rešujte nad tem komentarjem. ^^^ ###

import unittest

def fail_msg(args):
    return 'Failed on input: {}'.format(repr(args))

class TestVaje4(unittest.TestCase):
    def test_najdaljsa(self):
        in_out = [
            ('beseda', 'beseda'),
            ('an ban', 'ban'),
            ('an ban pet podgan', 'podgan'),
            ('an ban pet podgan stiri misi', 'podgan'),
            ('ta clanek je lepo napisan', 'napisan'),
            ('123456 12345 1234 123 12 1', '123456'),
            ('12345 123456 12345 1234 123 12 1', '123456'),
            ('1234 12345 123456 12345 1234 123 12 1', '123456'),
        ]

        for i, o in in_out:
            self.assertEqual(najdaljsa(i), o, fail_msg(i))

    def test_podobnost(self):
        in_out = [
            (('sobota', 'robot'), 4),
            (('', 'robot'), 0),
            (('sobota', ''), 0),
            (('', ''), 0),
            (('a', 'b'), 0),
            (('a', 'a'), 1),
            (('aaa', 'a'), 1),
            (('amper', 'amonijak'), 2),
            (('1000 let', 'tisoc let'), 0),
            (('hamming distance', 'haming  distance'), 12)
        ]
        
        for i, o in in_out:
            self.assertEqual(podobnost(*i), o, fail_msg(i))
            self.assertEqual(podobnost(*i[::-1]), o, fail_msg(i))
            
            

    def test_sumljive(self):
        in_out = [
            ('', []),
            ('aa uu', []),
            ('aa uu au', ['au']),
            ('muha', ['muha']),
            ('Muha pa je rekla: "Tale juha se je pa res prilegla, najlepša huala," in odletela.',
             ['Muha', 'juha', 'huala,"']),
            ('ameba nima aja in uja, ampak samo a', ['uja,']),
        ]

        for i, o in in_out:
            self.assertListEqual(sumljive(i), o, fail_msg(i))

    def test_vsi(self):
        in_out = [
            ([True, True, False], False),
            ([True, True], True),
            ([1, 2, 3, 0], False),
            (['foo', 42, True], True),
            (['foo', '', 42, True], False),
            (['foo', 0.0, 42, True], False),
            (['foo', None, 42, True], False),
            (['foo', (), 42, True], False),
            (['foo', [], 42, True], False),
            ([], True),
        ]

        for i, o in in_out:
            f = self.assertTrue if o else self.assertFalse
            f(vsi(i), fail_msg(i))

    def test_vsaj_eden(self):
        in_out = [
            ([2, 3, 0], True),
            ([], False),
            ([True, False, False], True),
            ([False, False], False),
            (['foo', 42, True], True),
            ([False, 0, 0.0, '', None, (), []], False),
            ([False, 0, 0.42, '', None, (), []], True),
            ([False, 0, 0.0, '', None, (), [42]], True),
        ]

        for i, o in in_out:
            f = self.assertTrue if o else self.assertFalse
            f(vsaj_eden(i), fail_msg(i))

    def test_emso(self):
        self.assertEqual(veljavna('2902932505526'), True)
        self.assertEqual(veljavna('2902932505525'), False)
        self.assertEqual(veljavna('2902932505524'), False)
        self.assertEqual(veljavna('2805985500156'), True)
        self.assertEqual(veljavna('2805985505156'), False)
        self.assertEqual(veljavna('2805985500155'), False)

    def test_drugi_najvecji(self):
        self.assertEqual(drugi_najvecji([5, 1, 4, 2, 3]), 4)
        self.assertEqual(drugi_najvecji([1, 1]), 1)
        self.assertEqual(drugi_najvecji([1, 2, 3]), 2)
        self.assertEqual(drugi_najvecji([4, 3, 2, 1]), 3)
        self.assertEqual(drugi_najvecji([4, 3, 2, 1, 8, 2, 3, 3, 9]), 8)

    def test_vsota_seznamov(self):
        in_out = [
            ([], []),
            ([[]], [0]),
            ([[0]], [0]),
            ([[1, 2]], [3]),
            ([[1, 2], [], [0]], [3, 0, 0]),
            ([[2, 4, 1], [3, 1], [], [8, 2], [1, 1, 1, 1]], [7, 4, 0, 10, 4]),
            ([[5, 3, 6, 3], [1, 2, 3, 4], [5, -1, 0]], [17, 10, 4]),
        ]

        for i, o in in_out:
            self.assertEqual(vsota_seznamov(i), o, fail_msg(i))

    def test_najvecji_podseznam(self):
        in_out = [
            ([[0]], [0]),
            ([[1, 2]], [1, 2]),
            ([[1, 2], [], [0]], [1, 2]),
            ([[2, 4, 1], [3, 1], [], [8, 2], [1, 1, 1, 1]], [8, 2]),
            ([[5, 3, 6, 3], [1, 2, 3, 4], [5, -1, 0]], [5, 3, 6, 3]),
        ]

        for i, o in in_out:
            self.assertEqual(najvecji_podseznam(i), o, fail_msg(i))

    def test_cezar(self):
        in_out = [
            ('', ''),
            ('a', 'd'),
            ('aa', 'dd'),
            ('ab', 'de'),
            ('z', 'c'),
            ('xyz', 'abc'),
            (' ', ' '),
            ('a  a', 'd  d'),
            ('julij cezar je seveda uporabljal cezarjevo sifro',
             'mxolm fhcdu mh vhyhgd xsrudeomdo fhcdumhyr vliur'),
            ('the quick brown fox jumps over the lazy dog',
             'wkh txlfn eurzq ira mxpsv ryhu wkh odcb grj'),
        ]

        for i, o in in_out:
            self.assertEqual(cezar(i), o, fail_msg(i))

    def test_mrange(self):
        in_out = [
            ((32, 2, 0), []),
            ((32, 2, 1), [32]),
            ((32, 2, 2), [32, 64]),
            ((42, -1, 5), [42, -42, 42, -42, 42]),
            ((7, 4, 7), [7, 28, 112, 448, 1792, 7168, 28672]),
        ]

        for i, o in in_out:
            self.assertListEqual(mrange(*i), o, fail_msg(i))


if __name__ == '__main__':
    unittest.main(verbosity=2)
