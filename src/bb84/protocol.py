from bb84.alice import encode_qubit, measure_qubit
def transmit(alice_bits: list[int], alice_bases: list[str], bob_bases: list[str]) -> list[int]:
    panier = []
    for i in range(len(alice_bits)):
        circuit = encode_qubit(alice_bits[i], alice_bases[i])
        resultat = measure_qubit(circuit, bob_bases[i])
        panier.append(resultat)
    return panier