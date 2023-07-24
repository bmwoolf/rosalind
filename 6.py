# hamming distance- number of symbols that are different


def hamming_distance(sequences):
    # require that the length of sequence[0] is the same as sequence[1]
    if len(sequences[0]) != len(sequences[1]):
        raise ValueError("both sequences must be the same length")
    
    distance = 0

    for i in range(len(sequences[0])):
        if sequences[0][i] != sequences[1][i]:
            distance += 1
    return distance

dna_sequences = [
    "GAGCCTACTAACGGGAT",
    "CATCGTAATGACGGCCT"
]

print(hamming_distance(dna_sequences))