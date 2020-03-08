

# cut-and-crossfill crossover for permutations
def permutation_cut_and_crossfill (parent1, parent2):

    offspring1 = []
    offspring2 = []

    # student code begin
    """
    offspring1 = parent1[:4] + parent2[4:]
    offspring2 = parent1[4:] + parent2[:4]
    """





    # student code end

    return offspring1, offspring2







######
list = [1,2,3,4,5,6,7,8]
offspring1 = list[:4]
offspring2 = list[4:]
print(offspring1)
print(offspring2)
