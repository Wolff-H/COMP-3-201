# COMP3201 - A genetic algorithm for Eight Queen puzzle
# by Ting Hu

# Assignment 2 - representation, fitness evalution, mutation, and crossover



import random
import numpy

import initialization
import evaluation
import recombination
import mutation

   
def main():
   
    # random.seed(0)
    # numpy.random.seed(0)

    string_length = 8
    popsize = 10
    mating_pool_size = int(popsize*0.5) # has to be even
    mut_rate = 1
    xover_rate = 0.9


    # initialize population
    population = initialization.permutation(popsize, string_length)
    fitness = []
    print("Initial population:")
    for i in range (0, popsize):
        fitness.append(evaluation.fitness_8queen(population[i]))
        print(i, ":", population[i],"fitness:", fitness[i])

    # pick parents
    parents_index = random.sample(range(0,popsize), mating_pool_size)    
    print("Parents:")
    for i in range (0, len(parents_index)):
        print(parents_index[i], ":", population[parents_index[i]])
        
    # reproduction
    offspring =[]
    i=0
    # offspring are generated using selected parents in the mating pool
    while len(offspring) < mating_pool_size:
        
        # recombination
        if random.random() < xover_rate:            
            off1,off2 = recombination.permutation_cut_and_crossfill(population[parents_index[i]], population[parents_index[i+1]])
        else:
            off1 = population[parents_index[i]].copy()
            off2 = population[parents_index[i+1]].copy()

        # print offspring after recombination 
        print("After xover:")
        print(off1,"fitness:", evaluation.fitness_8queen(off1))
        print(off2,"fitness:", evaluation.fitness_8queen(off2))
        
        if random.random() < mut_rate:
            off1 = mutation.permutation_swap(off1)
        if random.random() < mut_rate:
            off2 = mutation.permutation_swap(off2)
        
        # print offspring after mutation
        print("After mutation:")
        print(off1,"fitness:", evaluation.fitness_8queen(off1))
        print(off2,"fitness:", evaluation.fitness_8queen(off2))

        offspring.append(off1)
        offspring.append(off2)

# end of main


main()





