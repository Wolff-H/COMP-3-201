import random

# mutate a permutation
def permutation_swap (individual):
    
    #mutant = individual.copy()
    mutant = individual[:]

    # student code begin

    #generate two random postions
    locus1 = random.randint(0,7)
    locus2 = random.randint(0,7)

    #swap these two positions
    temp = mutant[locus1]
    mutant[locus1] = mutant[locus2]
    mutant[locus2] = temp
    

    # student code end
    
    return mutant

#test
"""
test = []
for i in range(0, 8):
    test.append(random.randint(1,8))
print(test)

test1 = permutation_swap(test)
print(test1)
"""