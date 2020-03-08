import random

# mutate a permutation


def permutation_swap (individual):
    
    mutant = individual.copy()

    # student code begin

    # random two positions
    x1 = random.randint(0, 7)
    x2 = random.randint(0, 7)

    # swap these two positions
    temp = mutant[x1]
    mutant[x1] = mutant[x2]
    mutant[x2] = temp

    # student code end
    
    return mutant
