# expected value :: E(X)=∑nk=1k×Pr(X=k)

# AA-AA, 1
# AA-Aa, 1
# AA-aa, 1
# Aa-Aa, 0.75
# Aa-aa, 0.5
# aa-aa, 0

def expected_offspring(num_couples):
    # for dominant allele
    probabilities = [1, 1, 1, 0.75, 0.5, 0]

    expected_offspring = 0
    # count of couples
    for i in range(6):
        expected_offspring += num_couples[i] * 2 * probabilities[i]
    return expected_offspring

num_couples = [1, 0, 0, 1, 0, 1]
print(expected_offspring(num_couples))