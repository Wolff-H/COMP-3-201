#by Ting Hu for COMP3201 A2

import random

# cut-and-crossfill crossover for permutations
def permutation_cut_and_crossfill (parent1, parent2):
    offspring1 = []
    offspring2 = []
    # student code begin
    l = len(parent1)
    twice1 = []
    twice2 = []
    for i in range (0, l):
        twice1.append(parent1[i])
        twice2.append(parent2[i])
    for i in range (0, l):
        twice1.append(parent1[i])
        twice2.append(parent2[i])
    xover_point = random.randint (1, l-2)
    #print("crossover point:", xover_point)
    
    for i in range (0, xover_point):
        offspring1.append(parent1[i])
        offspring2.append(parent2[i])

    j = xover_point
    while len(offspring1) < l:
        if twice2[j] in offspring1:
            j = j + 1
        else:
            offspring1.append(twice2[j])
            j = j + 1

    j = xover_point
    while len(offspring2) < l:
        if twice1[j] in offspring2:
            j = j + 1
        else:
            offspring2.append(twice1[j])
            j = j + 1
            
    # student code end
    return offspring1, offspring2
