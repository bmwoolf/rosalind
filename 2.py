inputDna = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
rna = ""

for i in inputDna:
    # print("i = ", i)
    if i == "T":
        rna += "U"
    else:
        rna += i

print(inputDna)
print(rna)