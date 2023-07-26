# Introduction to Mendelian Inheritance
# homozygous dominant: 2 copies of the same dominant allele for a gene
# heterozygous: 2 different alleles for a particular gene
# homozygous recessive: 2 copies of same recessive allele for a gene (blue eyes)

# math- remember we're going for *dominant* allele so the math will be tailored to getting that 
# AA and AA parents :: (k-1) :: k organism and k-1 to reproduce with
# AA and Aa or Aa and AA :: 2*k*m :: 2 possible orders, k and m such organisms
# AA and aa or aa and AA :: 2*k*n :: same as above but reverse
# Aa and Aa :: 0.75(m*(m-1)) :: only 75% chance of getting dominant allele, multiply by 0.75
# Aa and aa or aa and Aa :: 0.5(2*m*n) :: probability of picking this pair is 50%, so multiply by 0.5

def probability_dominant(k, m, n):
    # total population
    population = k + m + n

    # all possible paurs of parents
    total_pairs = population * (population - 1)

    # pairs that will prodcue dominant alleles
    dominant_pairs = k*(k-1) + 2*k*m + 2*k*n + 0.75*m*(m-1) + 0.5*2*m*n 

    # probability that offspring will have a dominant allele
    dominant_probability = dominant_pairs / total_pairs

    return dominant_probability


k, m, n = 2, 2, 2
print(probability_dominant(k, m, n))