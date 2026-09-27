from bb84.alice import random_bits, random_bases
from bb84.protocol import transmit, sift

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

def test_sift_deterministic():
    alice_bases = ["Z", "X", "Z", "X"]
    bob_bases = ["Z", "Z", "X", "X"]
    alice_bits = [0, 1, 1, 0]
    bob_results = [0, 0, 1, 0]
    cle_alice, cle_bob = sift(alice_bits, alice_bases, bob_bases, bob_results)
    assert cle_alice == [0, 0]
    assert cle_bob == [0, 0]
    assert len(cle_alice) == len(cle_bob)
    
def test_sift_statistical():
    liste_alice_bits = random_bits(1000)
    liste_alice_bases = random_bases(1000)
    liste_bob_bases = random_bases(1000)
    resultat_bob = transmit (liste_alice_bits, liste_alice_bases, liste_bob_bases)
    cle_alice, cle_bob = sift(liste_alice_bits, liste_alice_bases, liste_bob_bases, resultat_bob)
    valeur_alice = len(cle_alice)/1000
    assert valeur_alice >= 0.4
    assert valeur_alice <= 0.6

def test_protocol_v1_proof():
    liste_alice_bits = random_bits(1000)
    liste_alice_bases = random_bases(1000)
    liste_bob_bases = random_bases(1000)
    resultat_bob = transmit (liste_alice_bits, liste_alice_bases, liste_bob_bases)
    cle_alice, cle_bob = sift(liste_alice_bits, liste_alice_bases, liste_bob_bases, resultat_bob)
    assert cle_alice == cle_bob

def test_sift_with_eve():
    liste_alice_bits = random_bits(2000)
    liste_alice_bases = random_bases(2000)
    liste_bob_bases = random_bases(2000)
    resultat_bob = transmit (liste_alice_bits, liste_alice_bases, liste_bob_bases, eve=True)
    cle_alice, cle_bob = sift(liste_alice_bits, liste_alice_bases, liste_bob_bases, resultat_bob)
    nb_erreurs = 0
    for i in range(len(cle_alice)):
        if cle_alice[i] != cle_bob[i]:
            nb_erreurs = nb_erreurs + 1
    taux_erreurs = nb_erreurs / len(cle_alice)
    assert taux_erreurs >= 0.18
    assert taux_erreurs <= 0.32
