# list positions of a subset string in the main DNA
# pretty sure this is used for finding genes in a DNA sequence
# O(N) time complexity

dna = "GATATATGCATATACTT"
substring = "ATAT"
output = [2, 4, 10]

# prompt asks for 1 indexed- gross
def find_substring_locations(d, s):
    locations = []
    # loop- +1 at the end because you need to go past last place
    for i in range(len(d) - len(s) + 1): 
        if d[i:i+len(s)] == s:
            # positions are 1 indexed, not 0
            locations.append(i + 1)
    return locations

print(find_substring_locations(dna, substring))