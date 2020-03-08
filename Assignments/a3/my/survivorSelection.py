
import random



# (mu+lambda) selection
def mu_plus_lambda(current_pop, current_fitness, offspring, offspring_fitness):   
    population = []
    fitness = []

    # student code begin
    # print("current_pop",current_pop)
    # print("current_fitness",current_fitness)
    # print("offspring",offspring)
    # print("offspring_fitness",offspring_fitness)

    all_individuals = []
    all_individuals.extend(current_pop)
    all_individuals.extend(offspring)
    # print(all_individuals)
    all_fitness = []
    all_fitness.extend(current_fitness)
    all_fitness.extend(offspring_fitness)
    # print(all_fitness)

    i_with_info = {}
    for i in range( len(all_individuals) ) :
        i_with_info[i] = [ all_individuals[i], all_fitness[i] ]
    # print(i_with_info)

    ranked_i_with_info = sorted(i_with_info.items(), key=lambda item: item[1][1], reverse=True)
    # print("below is ranked i with info")
    # print(ranked_i_with_info)

    for i in range( len(current_pop) ) :
        population.append(ranked_i_with_info[i][1][0])
        fitness.append(ranked_i_with_info[i][1][1])

    # print(population)
    # print(fitness)

    # student code end
    
    return population, fitness


# use offspring to replace the same number of the worst individuals in the current population
def replacement(current_pop, current_fitness, offspring, offspring_fitness):
    
    population = []
    fitness = []
    
    # student code begin
    print("current_pop",current_pop)
    print("current_fitness",current_fitness)
    print("offspring",offspring)
    print("offspring_fitness",offspring_fitness)

    i_with_info = {}
    for i in range(len(current_pop)):
        i_with_info[i] = [current_pop[i], current_fitness[i]]
    print(i_with_info)

    ranked_i_with_info = sorted(i_with_info.items(), key=lambda item: item[1][1], reverse=True)
    print("below is ranked i with info")
    print(ranked_i_with_info)

    # print("###",range( len(current_pop)-len(offspring) ))
    for i in range( len(current_pop)-len(offspring) ) :
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
    # print(all_individuals)
    all_fitness = []
    all_fitness.extend(current_fitness)
    all_fitness.extend(offspring_fitness)
    # print(all_fitness)
    # print(range(len(all_individuals)))
    # print(len(current_pop))

    pointers = random.sample( range(len(all_individuals)), len(current_pop) )
    # print("pointers:",pointers)

    for index in pointers :
        population.append(all_individuals[index])
        fitness.append(all_fitness[index])



    # student code end
    
 
    return population, fitness
    


