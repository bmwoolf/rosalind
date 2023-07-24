input = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
output = ""

for i in input:
    # print("i = ", i)
    if i == "T":
        output += "U"
    else:
        output += i

print(input)
print(output)