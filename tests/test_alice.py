from bb84.alice import random_bits, random_bases
def test_longueur_bits():
    assert len(random_bits(10)) == 10

def test_valeurs_bits():
    for x in random_bits(20):
        assert x in [0, 1]

def test_longueur_bases():
    assert len(random_bases(10)) == 10

def test_valeurs_bases():
    for y in random_bases(20):
        assert y in ["X", "Z"]
