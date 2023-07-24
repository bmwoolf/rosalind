dna = "AAAACCCGGT"
complement = ""
# should be ACCGGGTTTT

for i in reversed_dna:
    if i == "A":
        complement += "T"
    elif i == "T":
        complement += "A"
    elif i == "C":
        complement += "G"
    elif i == "G":
        complement += "C"

print(complement)