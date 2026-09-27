import random
from qiskit import QuantumCircuit
from bb84.alice import encode_qubit, measure_qubit
def eve_intercept(circuit: QuantumCircuit) -> QuantumCircuit:
    eve_base = random.choice(["X", "Z"])
    eve_bit = measure_qubit(circuit, eve_base)
    reencode_eve = encode_qubit(eve_bit, eve_base)
    return reencode_eve