# FASTA formatting- way of storing DNA
# GC makes the molecule more stable- has 3 bonding pairs vs 2 for AT

from collections import defaultdict

def parse_fasta(fasta_array):
    parsed_dict = defaultdict(str)
    current_string = ""

    for fasta in fasta_array:
        for line in fasta.split("\n"):
            if line.startswith(">"):
                current_string = line[1:]
            else:
                parsed_dict[current_string] += line
    return parsed_dict

# calculate percentage of sequence that is GC
def gc_content(sequence):
    gc_count = sequence.count("G") + sequence.count("C")
    return (gc_count / len(sequence)) * 100

# get the highest number of GC content from input array + strings
def highest_gc_content(data):
    gc_contents = {key: gc_content(value) for key, value in data.items()}
    max_id = max(gc_contents, key=gc_contents.get)
    return max_id, gc_contents[max_id]

fasta_array = [
    ">Rosalind_6404\nCCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC\nTCCCACTAATAATTCTGAGG",
    ">Rosalind_5959\nCCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT\nATATCCATTTGTCAGCAGACACGC",
    ">Rosalind_0808\nCCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC\nTGGGAACCTGCGGGCAGTAGGTGGAAT",
]

data = parse_fasta(fasta_array)
result = highest_gc_content(data)

print(f"{result[0]}\n{result[1]:.6f}")