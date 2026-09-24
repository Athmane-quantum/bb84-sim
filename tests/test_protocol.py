from bb84.alice import random_bits, random_bases
from bb84.protocol import transmit

def test_length():
    liste_alice_bits = random_bits(10)
    list_alice_bases = random_bases(10)
    list_bob_bases = random_bases(10)
    resultat_bob = transmit (liste_alice_bits, list_alice_bases, list_bob_bases)
    assert len(resultat_bob) == len(liste_alice_bits)

def test_bits():
    liste_alice_bits = random_bits(10)
    list_alice_bases = random_bases(10)
    list_bob_bases = random_bases(10)
    resultat_bob = transmit (liste_alice_bits, list_alice_bases, list_bob_bases)
    for x in resultat_bob:
        assert x in [0, 1]

def test_transmit():
    liste_alice_bits = random_bits(10)
    list_alice_et_bob_bases = random_bases(10)
    resultat_bob = transmit (liste_alice_bits, list_alice_et_bob_bases, list_alice_et_bob_bases)
    assert resultat_bob == liste_alice_bits
