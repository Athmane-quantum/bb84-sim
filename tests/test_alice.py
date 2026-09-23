from bb84.alice import random_bits, random_bases , encode_qubit, measure_qubit
from qiskit.quantum_info import Statevector
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

def test_qubit0Z():
    circuit = encode_qubit(0, "Z")
    etat = Statevector.from_instruction(circuit)
    assert etat.equiv(Statevector.from_label("0"))

def test_qubit1Z():
    circuit = encode_qubit(1, "Z")
    etat = Statevector.from_instruction(circuit)
    assert etat.equiv(Statevector.from_label("1"))

def test_qubit0X():
    circuit = encode_qubit(0, "X")    
    etat = Statevector.from_instruction(circuit)
    assert etat.equiv(Statevector.from_label("+"))

def test_qubit1X():
    circuit = encode_qubit(1, "X")
    etat = Statevector.from_instruction(circuit)
    assert etat.equiv(Statevector.from_label("-"))

def test_qubit0X1X():
    circuit1 = encode_qubit(0, "X")
    circuit2 = encode_qubit(1, "X")
    etat1 = Statevector.from_instruction(encode_qubit(0, "X"))
    etat2 = Statevector.from_instruction(encode_qubit(1, "X"))
    assert not etat1.equiv(etat2)

def test_measure_qubit0Z():
    circuit = encode_qubit(0, "Z")
    resultat = measure_qubit(circuit, "Z")
    assert resultat == 0

def test_measure_qubit1Z():
    circuit = encode_qubit(1, "Z")
    resultat = measure_qubit(circuit, "Z")
    assert resultat == 1

def test_measure_qubit0X():
    circuit = encode_qubit(0, "X")
    resultat = measure_qubit(circuit, "X")
    assert resultat == 0

def test_measure_qubit1X():
    circuit = encode_qubit(1, "X")
    resultat = measure_qubit(circuit, "X")
    assert resultat == 1

def test_measure_qubit_Alice():
    circuit1 = encode_qubit(0, "Z")
    etat1 = Statevector.from_instruction(circuit1)
    measure_qubit(circuit1, "X")
    etat2 = Statevector.from_instruction(circuit1)
    assert etat1.equiv(etat2)