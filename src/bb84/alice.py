import random
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
def random_bits(n):
    bits = []
    for i in range(n):
        bits.append(random.randint(0, 1))
    return bits

def random_bases(n):
    bases = []
    for i in range(n):
        bases.append(random.choice(["X", "Z"]))
    return bases

def encode_qubit(bit: int, basis: str) -> QuantumCircuit:
    qc = QuantumCircuit(1)
    if bit == 1 and basis == "Z":
        qc.x(0)
    elif bit == 0 and basis == "X":
        qc.h(0)
    elif bit == 1 and basis == "X":
        qc.x(0) 
        qc.h(0)
    return qc

def measure_qubit(circuit: QuantumCircuit, basis: str) -> int:
    qc = circuit.copy()
    if basis == "X":
        qc.h(0)
    sv = Statevector.from_instruction(qc)
    resultat, etat = sv.measure()  
    return int(resultat)