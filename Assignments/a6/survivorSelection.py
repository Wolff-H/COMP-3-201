
import random



# (mu+lambda) selection
def mu_plus_lambda(current_pop, current_fitness, offspring, offspring_fitness):   
    population = []
    fitness = []

    # joint parents and offspring #
    all_individuals = []
    all_individuals.extend(current_pop)
    all_individuals.extend(offspring)
    all_fitness = []
    all_fitness.extend(current_fitness)
    all_fitness.extend(offspring_fitness)

    # dict { index: [layout,fitness] } #
    i_with_info = {}
    for i in range( len(all_individuals) ) :
        i_with_info[i] = [ all_individuals[i], all_fitness[i] ]

    # i_with_info ranked by item.fitness #
    ranked_i_with_info = sorted(i_with_info.items(), key=lambda item: item[1][1], reverse=True)

    # μ+λ #
    for i in range( len(current_pop) ) :
        population.append(ranked_i_with_info[i][1][0])
        fitness.append(ranked_i_with_info[i][1][1])

    # student code end
    
    return population, fitness


# use offspring to replace the same number of the worst individuals in the current population
def replacement(current_pop, current_fitness, offspring, offspring_fitness):
    
    population = []
    fitness = []
    
    # student code begin

    i_with_info = {}
    for i in range(len(current_pop)):
        i_with_info[i] = [current_pop[i], current_fitness[i]]

    ranked_i_with_info = sorted(i_with_info.items(), key=lambda item: item[1][1], reverse=True)

    for i in range( len(current_pop)-len(offspring)+1 ) :
        population.append(ranked_i_with_info[i][1][0])
        fitness.append(ranked_i_with_info[i][1][1])

    population.extend(offspring)
    fitness.extend(offspring_fitness)


    # student code end
    
    return population, fitness


# randomly uniformly pick individuals from the current population and new offspring
def random_uniform(current_pop, current_fitness, offspring, offspring_fitness):
    
    population = []
    fitness = []

    # student code begin

    all_individuals = []
    all_individuals.extend(current_pop)
    all_individuals.extend(offspring)
    all_fitness = []
    all_fitness.extend(current_fitness)
    all_fitness.extend(offspring_fitness)

    pointers = random.sample( range(len(all_individuals)), len(current_pop) )

    for index in pointers :
        population.append(all_individuals[index])
        fitness.append(all_fitness[index])

    # student code end
    
 
    return population, fitness
    


