# rabbit pairs per generation

input = [6, 3]
# output = [4]

def rabbits(params):
    # unpack params, could make it modular to do unlimited 
    n, m = params

    rabbit_pairs = [0]*n
    rabbit_pairs[0] = 1
    for i in range(1, n):
        if i < m:
            if i == 1:
                rabbit_pairs[i] = 1
            else:
                rabbit_pairs[i] = rabbit_pairs[i-1] + rabbit_pairs[i-2]
        elif i == m:
            rabbit_pairs[i] = rabbit_pairs[i-1] + rabbit_pairs[i-2] - 1
        else:
            rabbit_pairs[i] = rabbit_pairs[i-1] + rabbit_pairs[i-2] - rabbit_pairs[i-m-1]
    return rabbit_pairs[-1]

print(rabbits(input))