import collections
#inventar
def zaloga(inventar, artikel):
    return inventar[artikel]
def prodaj(inventar, artikel, kolicina):
    inventar[artikel]=zaloga(inventar,artikel)-kolicina
def primanjkljaj(inventar, narocilo):
    new_dict={}
    for hrana,stevilo in narocilo.items():
        if hrana not in inventar:
            new_dict[hrana]=stevilo
        elif stevilo>inventar[hrana]:
            new_dict[hrana]=stevilo-inventar[hrana]
    return new_dict
#najpogostejše
def freq(s):
    diction={}
    for i in s:
        if i not in diction:
            diction[i]=1
        else:diction[i]+=1
    return diction
def max_freq(s):
    return max(freq(s), key=freq(s).get)
def najpogostejse(s):
    a=s.split()
    return max_freq(a),max_freq(s)

def najpogostejse_urejene(s):
    sez=[]
    sez2=[]
    sort_orders = sorted(freq(s).items(), key=lambda x: (-x[1], x[0]))
    for i in sort_orders:
        if i[0] not in sez:
            sez.append(i[0])
    a=s.split()
    a=freq(a)
    sort_orders2 = sorted(a.items(), key=lambda x: (-x[1], x[0]))
    for i in sort_orders2:
        if i[0] not in sez2:
            sez2.append(i[0])
    return sez2, sez
#družinsko drevo
def family_tree(family):
    slovar={}
    for i in family:
        if i[0] not in slovar:
            slovar[i[0]]=[i[1]]
        else:
            slovar[i[0]].append(i[1])
    return slovar

def children(tree, name):
    if name not in tree:
        return []
    return tree[name]

def grandchildren(tree, name):
    new_list=[]
    for i in children(tree,name):
        new_list+=children(tree,i)
    return new_list
def successors(tree, name):
    new_sez=children(tree,name)
    for i in new_sez:
        new_sez=new_sez+children(tree,i)
###naključno genererano besedilo
def nasledniki(txt):
    a=txt.split()
    bou={}

    return bou



### ^^^ Naloge rešujte nad tem komentarjem. ^^^ ###

import unittest
import collections

class TestSlovarji(unittest.TestCase):
    def setUp(self):
        self.tree = {
            'alice': ['mary', 'tom', 'judy'],
            'bob': ['mary', 'tom', 'judy'],
            'ken': ['suzan'],
            'renee': ['rob', 'bob'],
            'rob': ['jim'],
            'sid': ['rob', 'bob'],
            'tom': ['ken']}

    def assertDictCounterEqual(self, first, second, msg=None):
        def dict_counter(d):
            d_copy = dict(d)
            for k, v in d_copy.items():
                d_copy[k] = collections.Counter(v)
            return d_copy
        self.assertDictEqual(dict_counter(first), dict_counter(second), msg)

    def test_zaloga(self):
        inv = {"kruh": 5, "kajzerica": 4, "makovka": 3}
        self.assertEqual(zaloga(inv, "kruh"), 5)
        self.assertEqual(zaloga(inv, "kajzerica"), 4)
        self.assertEqual(zaloga(inv, "makovka"), 3)

    def test_prodaj(self):
        inv = {"kruh": 5, "kajzerica": 4, "makovka": 3}
        self.assertIsNone(prodaj(inv, "kajzerica", 2), "Funkcija naj ne vrača ničesar!")
        self.assertEqual(zaloga(inv, "kruh"), 5)
        self.assertEqual(zaloga(inv, "kajzerica"), 2)
        self.assertEqual(zaloga(inv, "makovka"), 3)

        prodaj(inv, "kruh", 5)
        self.assertTrue("kruh" not in inv or (zaloga(inv, "kruh"), 0))
        self.assertEqual(zaloga(inv, "kajzerica"), 2)
        self.assertEqual(zaloga(inv, "makovka"), 3)

    def test_primanjkljaj(self):
        inventar = {
            'sir': 8, 'kruh': 15, 'makovka': 10, 'pasja radost': 2,
            'pašteta': 10, 'mortadela': 4, 'klobasa': 7
        }
        self.assertDictEqual(
            primanjkljaj(inventar, {"kruh": 2, "makovka": 10}),
            {})
        self.assertDictEqual(
            primanjkljaj(inventar, {"kruh": 2, "makovka": 12}),
            {"makovka": 2})
        self.assertDictEqual(
            primanjkljaj(inventar, {"kruh": 2, "makovka": 12, "pivo": 3}),
            {"makovka": 2, "pivo": 3})
        self.assertDictEqual(primanjkljaj(inventar, {}), {})
        self.assertDictEqual(primanjkljaj(inventar, inventar), {})

    def test_family_tree(self):
        family = [
            ('bob', 'mary'),
            ('bob', 'tom'),
            ('bob', 'judy'),
            ('alice', 'mary'),
            ('alice', 'tom'),
            ('alice', 'judy'),
            ('renee', 'rob'),
            ('renee', 'bob'),
            ('sid', 'rob'),
            ('sid', 'bob'),
            ('tom', 'ken'),
            ('ken', 'suzan'),
            ('rob', 'jim')]
        self.assertDictCounterEqual(family_tree(family), self.tree)

    def test_children(self):
        self.assertCountEqual(children(self.tree, 'alice'), ['mary', 'tom', 'judy'])
        self.assertCountEqual(children(self.tree, 'mary'), [])
        self.assertCountEqual(children(self.tree, 'renee'), ['bob', 'rob'])
        self.assertCountEqual(children(self.tree, 'rob'), ['jim'])
        self.assertCountEqual(children(self.tree, 'suzan'), [])

    def test_grandchildren(self):
        self.assertCountEqual(grandchildren(self.tree, 'alice'), ['ken'])
        self.assertCountEqual(grandchildren(self.tree, 'bob'), ['ken'])
        self.assertCountEqual(grandchildren(self.tree, 'ken'), [])
        self.assertCountEqual(grandchildren(self.tree, 'mary'), [])
        self.assertCountEqual(grandchildren(self.tree, 'renee'), ['jim', 'mary', 'tom', 'judy'])
        self.assertCountEqual(grandchildren(self.tree, 'sid'), ['jim', 'mary', 'tom', 'judy'])
        self.assertCountEqual(grandchildren(self.tree, 'tom'), ['suzan'])

    def test_successors(self):
        self.assertCountEqual(successors(self.tree, 'tom'), ['ken', 'suzan'])
        self.assertCountEqual(successors(self.tree, 'sid'),
            ['rob', 'bob', 'jim', 'mary', 'tom', 'judy', 'ken', 'suzan'])
        self.assertCountEqual(successors(self.tree, 'suzan'), [])
        self.assertCountEqual(successors(self.tree, 'ken'), ['suzan'])
        self.assertCountEqual(successors(self.tree, 'rob'), ['jim'])

    def test_najpogostejse(self):
        self.assertEqual(najpogostejse('a'), ('a', 'a'))
        self.assertEqual(najpogostejse('aa bb aa'), ('aa', 'a'))
        self.assertEqual(najpogostejse('in to in ono in to smo mi'), ('in', ' '))
        self.assertEqual(najpogostejse('abc abc abc abacbca'), ('abc', 'a'))
        self.assertEqual(najpogostejse('abc abc abc abacbcb'), ('abc', 'b'))
        self.assertEqual(najpogostejse('abc abc abc abacbcc'), ('abc', 'c'))

    def test_najpogostejse_urejene(self):
        self.assertEqual(najpogostejse_urejene('a'), (['a'], ['a']))
        self.assertEqual(najpogostejse_urejene('aa bb aa'), (['aa', 'bb'], ['a', ' ', 'b']))
        self.assertEqual(najpogostejse_urejene('in to in ono in to smo mi'),
            (['in', 'to', 'mi', 'ono', 'smo'], [' ', 'o', 'i', 'n', 'm', 't', 's']))
        self.assertEqual(najpogostejse_urejene('abc abc abc abacbca'),
            (['abc', 'abacbca'], ['a', 'b', 'c', ' ']))
        self.assertEqual(najpogostejse_urejene('abc abc abc abacbcb'),
            (['abc', 'abacbcb'], ['b', 'a', 'c', ' ']))
        self.assertEqual(najpogostejse_urejene('abc abc abc abacbcc'),
            (['abc', 'abacbcc'], ['c', 'a', 'b', ' ']))

    def test_sifra(self):
        self.assertEqual(sifra('\x19\x14\x1c]\x19\x0f\x14\t\x13\x18\t]\x12\x0e[\n\x1a\t\x18\x15\x12\x13\x1c'),
            'big brother is watching')
        self.assertEqual(sifra('\xe1d\xe0q\xe5r\xf7b\xe0i'), 'strawberry')

    def test_nasledniki(self):
        self.assertDictCounterEqual(nasledniki('in in in in'), {'in': ['in', 'in', 'in']})
        self.assertDictCounterEqual(nasledniki('in to in ono in to smo mi'),
            {'smo': ['mi'], 'to': ['in', 'smo'], 'ono': ['in'], 'in': ['to', 'ono', 'to']})
        self.assertDictCounterEqual(nasledniki('danes je lep dan danes sije sonce'),
            {'lep': ['dan'], 'je': ['lep'], 'dan': ['danes'], 'danes': ['je', 'sije'], 'sije': ['sonce']})

    def test_tekst(self):
        self.assertEqual(tekst({'in': ['in', 'in']}, 3), 'in in in')

if __name__ == '__main__':
    unittest.main(verbosity=2)
