# find the most likely common ancestor- prob used by Ancestry and 23&me
# consensus string = the most common letter (nucleotide) at each position in the profile matrix
# time complexity is O(M*N)

# DNA Strings
# A T C C A G C T...
# G G G C A A C T...
# A T G G A T C T...
# A A G C A A C C...
# T T G G A A C T...
# A T G C C A T T...
# A T G G C A C T...

# find the count of each letter at each position- O(N), could be 3.2B for each genome
# A: 5 1 0 0 5 5 0 0...
# C: 0 0 1 4 2 0 6 1...
# G: 1 1 6 3 0 1 0 0...
# T: 1 5 0 0 0 1 1 6...

# collection of DNA strings- would be a lot with compute
dna_strings = [
    "ATCCAGCT",
    "GGGCAACT",
    "ATGGATCT",
    "AAGCAACC",
    "TTGGAACT",
    "ATGCCATT",
    "ATGGCACT"
]

def consensus_and_profile(strings):
    # initialize matrix with 0's
    profile = {
        "A": [0]*len(strings[0]), 
        "C": [0]*len(strings[0]),
        "G": [0]*len(strings[0]),
        "T": [0]*len(strings[0])
    }

    # iterate through matrix
    for string in strings:
        for j, char in enumerate(string):
            profile[char][j] += 1
    
    consensus = []
    for j in range(len(strings[0])):
        max_count = max(
            profile["A"][j], 
            profile["C"][j], 
            profile["G"][j], 
            profile["T"][j]
        )

        for char in "ACGT":
            if profile[char][j] == max_count:
                consensus.append(char)
                break
        return "".join(consensus), profile

consensus, profile = consensus_and_profile(dna_strings)
for char in "ACGT":
    print(f'{char}: {" ".join(map(str, profile[char]))}')

