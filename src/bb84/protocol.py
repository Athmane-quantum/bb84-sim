from bb84.alice import encode_qubit, measure_qubit
from bb84.eve import eve_intercept
def transmit(alice_bits: list[int], alice_bases: list[str], bob_bases: list[str], eve: bool = False) -> list[int]:
    panier = []
    for i in range(len(alice_bits)):
        circuit = encode_qubit(alice_bits[i], alice_bases[i])
        if eve == True:
            circuit = eve_intercept(circuit)
        resultat = measure_qubit(circuit, bob_bases[i])
        panier.append(resultat)
    return panier

def sift(alice_bits: list[int], alice_bases: list[str], bob_bases: list[str], bob_results: list[int]) -> tuple[list[int], list[int]]:
    alice_key = []
    bob_key = []
    for i in range(len(alice_bases)):
        if alice_bases[i] == bob_bases[i]:
            alice_key.append(alice_bits[i])
            bob_key.append(bob_results[i])
    return alice_key, bob_key

def qber(alice_key: list[int], bob_key: list[int]) -> float:
    if len(alice_key) == 0:
        raise ValueError("clé vide : QBER indéfini")
    nb_erreurs = 0
    for i in range(len(alice_key)):
        if alice_key[i] != bob_key[i]:
            nb_erreurs = nb_erreurs + 1
    taux_erreurs = nb_erreurs / len(alice_key)
    return taux_erreurs

