# overlap graph for DNA strings
# basically a DAG for the highest letters- so if one strand ends with AAA and the next begins with AAA theyll the first will point to the second
# if there are multiple, it will be a single node for the preceding node pointing to the others

fasta = """
>Rosalind_0498
AAATAAA
>Rosalind_2391
AAATTTT
>Rosalind_2323
TTTTCCC
>Rosalind_0442
AAATCCC
>Rosalind_5013
GGGTGGG
"""

def fasta_to_dict(fasta_list):
    fasta_dict = {}
    for line in fasta_list:
        if line[0] == '>':
            key = line[1:]
            fasta_dict[key] = ""
        else:
            fasta_dict[key] += line
    return fasta_dict

def overlap_graph(fasta, n):
    result = []
    # fasta.items()- array of tuples: ('Rosalind_0498', 'AAATAAA')
    for k1, v1 in fasta.items():
        for k2, v2 in fasta.items():
            if k1 != k2 and v1.endswith(v2[:n]):
                result.append((k1,k2))
    return result

# splitting the fasta string into lines and passing it to the fasta_to_dict function
fasta_dict = fasta_to_dict(fasta.strip().split('\n'))
graph = overlap_graph(fasta_dict, 3)

for edge in graph:
    print(" ".join(edge))
