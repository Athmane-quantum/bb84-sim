import matplotlib.pyplot as plt
from bb84 import random_bits, random_bases, transmit, sift, qber

N_BITS = 500
N_RUNS = 10

qber_sans_eve = []
qber_avec_eve = []

for _ in range(N_RUNS):
    alice_bits = random_bits(N_BITS)
    alice_bases = random_bases(N_BITS)
    bob_bases = random_bases(N_BITS)

    resultats = transmit(alice_bits, alice_bases, bob_bases)
    cle_alice, cle_bob = sift(alice_bits, alice_bases, bob_bases, resultats)
    qber_sans_eve.append(qber(cle_alice, cle_bob))

    resultats = transmit(alice_bits, alice_bases, bob_bases, eve=True)
    cle_alice, cle_bob = sift(alice_bits, alice_bases, bob_bases, resultats)
    qber_avec_eve.append(qber(cle_alice, cle_bob))

moyenne_sans = sum(qber_sans_eve) / len(qber_sans_eve)
moyenne_avec = sum(qber_avec_eve) / len(qber_avec_eve)

print(f"QBER moyen sans Ève : {moyenne_sans:.1%}")
print(f"QBER moyen avec Ève : {moyenne_avec:.1%}")

plt.bar(["No eavesdropper", "Eve (intercept-resend)"],
        [moyenne_sans, moyenne_avec], color=["#4c9a6a", "#c0504d"])
plt.axhline(0.11, linestyle="--", color="gray", label="Abort threshold (~11%)")
plt.ylabel("QBER")
plt.ylim(0, 0.35)
plt.title(f"BB84: mean QBER over {N_RUNS} runs of {N_BITS} qubits")
plt.legend()
plt.savefig("docs/qber.png", dpi=150)
print("Graphe enregistré dans docs/qber.png")