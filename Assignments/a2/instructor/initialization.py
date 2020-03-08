#by Ting Hu for COMP3201 A2

import numpy

# initialize a population of permutation
def permutation (pop_size, chrom_length):
    
    population = []
    # student code begin

    for i in range (0, pop_size):
        population.append(numpy.random.permutation(chrom_length))

    #student code end                    
    return population                     

