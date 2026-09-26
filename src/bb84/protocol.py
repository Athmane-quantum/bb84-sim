from bb84.alice import encode_qubit, measure_qubit
def transmit(alice_bits: list[int], alice_bases: list[str], bob_bases: list[str]) -> list[int]:
    panier = []
    for i in range(len(alice_bits)):
        circuit = encode_qubit(alice_bits[i], alice_bases[i])
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