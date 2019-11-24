import itertools


def compute(polynomial, input_register):
    output = len(input_register) * [None]
    
    output[1:] = input_register[:-1]

    xor = 0
    for i in range(len(polynomial)):
        if polynomial[i] == 1:
            xor ^= input_register[i]

    output[0] = xor

    return output


registers = list(itertools.product([0, 1], repeat=8))
polynomials = set(itertools.permutations([0, 0, 0, 0, 0, 1, 1, 1]))


k = 0
for polynomial in polynomials:

    # First check for reversibility
    outputs = set()
    for register in registers:
        outputs.add(tuple(compute(polynomial, register)))

    reversible = len(outputs) == len(registers)

    if not reversible:
        continue

    print(polynomial)

    # Check for cycle lengths
    cycle_lengths = set()
    for register in registers:

        temp_register = list(register)

        i = 0
        while True:
            i += 1
            temp_register = compute(polynomial, temp_register)

            if tuple(temp_register) == register:
                cycle_lengths.add(i)
                break

    print(cycle_lengths)
    if 255 in cycle_lengths:
        k += 1
    print('---------------------')

print(k)