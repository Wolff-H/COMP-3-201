import random
import evaluation
import operator


def sort_population(population, fitness): # sort a population based on fitness, from max to min
    pop_fit_pair = list(map(list,zip(population, fitness)))
    pop_fit_pair.sort(key=operator.itemgetter(1), reverse=True)
    sorted_pop = []
    sorted_fit = []
    for entry in pop_fit_pair:
        sorted_pop.append(entry[0])
        sorted_fit.append(entry[1])
    return sorted_pop, sorted_fit


def mu_plus_lambda(current_pop, current_fitness, offspring, offspring_fitness):   
    population = []
    fitness = []
    temp_pop = current_pop.copy() + offspring.copy()
    temp_fit = current_fitness.copy() + offspring_fitness.copy()
    sorted_pop, sorted_fit = sort_population(temp_pop, temp_fit)
    for i in range(0,len(current_pop)):
        population.append(sorted_pop[i])
        fitness.append(sorted_fit[i])
    return population, fitness


def replacement(current_pop, current_fitness, offspring, offspring_fitness):
    population = []
    fitness = []
    sorted_pop, sorted_fit = sort_population(current_pop.copy(), current_fitness.copy())
    k = len(current_pop) - len(offspring)
    for i in range(0,k):
        population.append(sorted_pop[i])
        fitness.append(sorted_fit[i])
    for j in range(0,len(offspring)):
        population.append(offspring[j])
        fitness.append(offspring_fitness[j])       
    return population, fitness


def random_uniform(current_pop, current_fitness, offspring, offspring_fitness):
    population = []
    fitness = []
    temp_pop = current_pop.copy() + offspring.copy()
    temp_fit = current_fitness.copy() + offspring_fitness.copy()
    pick_index = random.sample(range(0,len(temp_pop)), len(current_pop))
    for i in range(0,len(pick_index)):
        population.append(temp_pop[pick_index[i]])
        fitness.append(temp_fit[pick_index[i]])
    return population, fitness
    


