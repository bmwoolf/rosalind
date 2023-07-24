input = list("AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC")

obj = {
    "A": 0,
    "T": 0,
    "C": 0,
    "G": 0
}

print(input)
print(type(input))

for i in input:
    if i in obj:
        obj[i] += 1

output = [obj["A"], obj["T"], obj["C"], obj["G"]]
print(output)