# COMP3201 - A genetic algorithm for Eight Queen puzzle
# by Ting Hu

# Assignment 3 - parent selection and survivor selection



import random
import numpy
import json

import initialization
import evaluation
import recombination
import mutation
import parentSelection
import survivorSelection

   
def main():

    experiment = [
        # nothing yet
    ]

    stat = ["mean", "std", "aes", "sr"]

    evos = 0

    while evos < 20:

        trial = [-1, []]    # [seccessed-generatiohn, best-fitness]
        recorded = False


        random.seed()
        numpy.random.seed()

        string_length = 8
        popsize = 20    # original 20
        mating_pool_size = int(popsize*0.5) # has to be even
        tournament_size = 4
        mut_rate = 0.2
        xover_rate = 0.9
        gen_limit = 50

        # initialize population
        gen = 0 # initialize the generation counter
        population = initialization.permutation(popsize, string_length)
        fitness = []
        for i in range(0, popsize):
            fitness.append(evaluation.fitness_8queen(population[i]))
        print("generation", gen, ": best fitness", max(fitness), "average fitness", sum(fitness)/len(fitness))

        # evolution begins
        while gen < gen_limit:

            # pick parents
            #parents_index = parentSelection.MPS(fitness, mating_pool_size)
            parents_index = parentSelection.tournament(fitness, mating_pool_size, tournament_size)
            #parents_index = parentSelection.random_uniform(popsize, mating_pool_size)

            # in order to randomly pair up parents
            random.shuffle(parents_index)

            # reproduction
            offspring =[]
            offspring_fitness = []
            i= 0 # initialize the counter for parents in the mating pool
            # offspring are generated using selected parents in the mating pool
            while len(offspring) < mating_pool_size:

                # recombination
                if random.random() < xover_rate:
                    off1,off2 = recombination.permutation_cut_and_crossfill(population[parents_index[i]], population[parents_index[i+1]])
                else:
                    off1 = population[parents_index[i]].copy()
                    off2 = population[parents_index[i+1]].copy()

                # mutation
                if random.random() < mut_rate:
                    off1 = mutation.permutation_swap(off1)
                if random.random() < mut_rate:
                    off2 = mutation.permutation_swap(off2)

                offspring.append(off1)
                offspring_fitness.append(evaluation.fitness_8queen(off1))
                offspring.append(off2)
                offspring_fitness.append(evaluation.fitness_8queen(off2))
                i = i+2  # update the counter

            # form the population of next generation
            population, fitness = survivorSelection.mu_plus_lambda(population, fitness, offspring, offspring_fitness)
    #        population, fitness = survivorSelection.replacement(population, fitness, offspring, offspring_fitness)
    #        population, fitness = survivorSelection.random_uniform(population, fitness, offspring, offspring_fitness)

            gen = gen + 1  # update the generation counter
            print("generation", gen, ": best fitness", max(fitness), "average fitness", sum(fitness)/len(fitness))

            trial[1].append( max(fitness) )
            #trial[1].append( sum(fitness)/len(fitness) )

            if max(fitness) == 28 and recorded == False:
                trial[0] = gen + 1
                recorded = True

        # evolution ends

        # print the final best solution(s)
        k = 0
        for i in range (0, popsize):
            if fitness[i] == max(fitness):
                print("best solution", k, population[i], fitness[i])
                k = k+1

        evos = evos + 1
        experiment.append(trial)

    bests = []
    sr = []

    for trial in experiment:
        final = trial[1][49]
        bests.append(final)

        if trial[0] != -1:
            sr.append(trial[0])

    stat[0] = numpy.mean(bests)
    stat[1] = numpy.std(bests)
    stat[3] = sr
    stat[2] = numpy.mean(stat[3])




    output_file = open("trace.js", "a")

    output_file.write("let tourn_miu = ")
    output_file.write(json.dumps(experiment))
    output_file.write(";\n")
    output_file.write("let tourn_miu_stat = ")
    output_file.write(json.dumps(stat))
    output_file.write(";\n")

    output_file.close()
# end of main




main()





