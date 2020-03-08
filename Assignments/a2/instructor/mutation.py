#by Ting Hu for COMP3201 A2

import random

# mutate a permutation
def permutation_swap (individual):
    mutant = individual.copy()
    mutation_points = random.sample(range(len(individual)), 2)
    mutant[mutation_points[0]] = individual[mutation_points[1]]
    mutant[mutation_points[1]] = individual[mutation_points[0]]         
    return mutant
