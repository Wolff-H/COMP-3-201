
import random

# cut-and-crossfill crossover for permutations
def permutation_cut_and_crossfill (parent1, parent2):
    
    offspring1 = []
    offspring2 = []
    
    # student code begin

    """
        random a cut point:
        12345678
        _|
        _______|    <= largest range(not include cut-point itself)
        01234567    cut fragment from parent[0] to parent[4]
        
        slice a layout to [ parent_a + parent_b ]
    """
    cut_point = random.randint(1, 7)

    p1a = parent1[:cut_point]
    p1b = parent1[cut_point:]
    p2a = parent2[:cut_point]
    p2b = parent2[cut_point:]

    offspring1 = p1a + p2b
    offspring2 = p2a + p1b

    return offspring1, offspring2
