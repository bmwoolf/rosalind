# longest common substrings

def read_fasta(data):
    strings = data.strip().split('>')[1:]
    strings = [s[s.index('\n')+1:].replace('\n', '') for s in strings]
    return strings

def longest_common_substring(strings):
    # sort strings by length
    sorted_strings = sorted(strings, key=len)
    
    # check substrings of the shortest string from longest -> shortest
    for length in range(len(sorted_strings[0]), 0, -1):
        for start_pos in range(len(sorted_strings[0]) - length + 1):
            match = sorted_strings[0][start_pos:start_pos + length]
            if all(match in x for x in sorted_strings):
                return match

data = """>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA"""

strings = read_fasta(data)
print(longest_common_substring(strings))
