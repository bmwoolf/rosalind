def rabbit_pairs(n, k):
    pairs = [1, 1]

    for i in range(2, n):
        new_pairs = pairs[i - 2] * k #mature bunnies reproducing, not new ones. go back 2
        mature_pairs = pairs[i - 1]
        total_pairs = mature_pairs + new_pairs
        pairs.append(total_pairs)
    
    return pairs[-1]

n = 5
k = 3

result = rabbit_pairs(n, k)
print(result)