
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
        ____|       <= largest range(not include cut-point itself)
        01234567    cut fragment from parent[0] to parent[4]
        
        slice a layout to [ parent_a + parent_b ]
        
        mechanism:
            p1a p1b            p1a p2a p1b_diff_p2a
            135|26668    ->    135|876¦24
            876|54321    ->    876|135¦42
            p2a p2b            p2a p1a p2b_diff_p1a
    """
    cut_point = random.randint(1, 4)

    p1a = parent1[:cut_point]
    p1b = parent1[cut_point:]
    p2a = parent2[:cut_point]
    p2b = parent2[cut_point:]

    p1b_diff_p2a = p1b.copy()
    for num in p2a :
        if num in p1b_diff_p2a :
            p1b_diff_p2a.remove(num)

    p2b_diff_p1a = p2b.copy()
    for num in p1a :
        if num in p2b_diff_p1a :
            p2b_diff_p1a.remove(num)

    # use numbers exactly from itself to fill itself
    offspring1 = p1a+p2a
    j = 0
    while len(offspring1) < 8 :
        offspring1.append(p1b_diff_p2a[j])
        j = j + 1

    offspring2 = p2a+p1a
    k = 0
    while len(offspring2) < 8 :
        offspring2.append(p2b_diff_p1a[k])
        k = k + 1


    # print(cut_point)
    # print("p1:", p1a, p1b, p1b_diff_p2a)
    # print("p2:", p2a, p2b, p2b_diff_p1a)
    # print("offspring1:", p1a, p2a, offspring1)
    # print("offspring2:", p2a, p1a, offspring2)
    # student code end

    return offspring1, offspring2


"""
    test here
"""
"""
parent = [2, 8, 5, 7, 1, 4, 3, 6]

print( parent[:4] )
print( parent[4:] )
# print( [1, 2, 3, 4] - [2, 3] )

p1b_diff_p2a = [2, 6, 4, 7, 8]

for num in [8, 7, 6] :
    if num in p1b_diff_p2a :
        p1b_diff_p2a.remove(num)

print(p1b_diff_p2a)
"""