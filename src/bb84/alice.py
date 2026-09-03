import random
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