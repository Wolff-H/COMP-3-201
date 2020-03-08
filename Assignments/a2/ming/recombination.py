import random

# cut-and-crossfill crossover for permutations
def permutation_cut_and_crossfill (parent1, parent2):
    
    offspring1 = []
    offspring2 = []
    
    # student code begin

    #choose random crossover point
    cross_point = random.randint(0,7)

    parent1_left = []
    parent1_right = []
    parent2_left = []
    parent2_right = []
    new_parent1_right = []
    new_parent2_right = []

    #cut the parents into left and right
    for i in range(0, cross_point):
        parent1_left.append(parent1[i])
        parent2_left.append(parent2[i])

    for i in range(cross_point, len(parent1)):
        parent1_right.append(parent1[i])
        parent2_right.append(parent2[i])

    #crossfill
    for i in range(len(parent2_right)):
        if parent2_right[i] not in parent1_left:
            new_parent1_right.append(parent2_right[i])
        if parent1_right[i] not in parent2_left:
            new_parent2_right.append(parent1_right[i])

    for allele in parent2_left:
        if len(new_parent1_right) < len(parent1_right):
            new_parent1_right.append(allele)


    for allele in parent1_left:
        if len(new_parent2_right) < len(parent2_right):
            new_parent2_right.append(allele)

    offspring1 = parent1_left + new_parent1_right
    offspring2 = parent2_left + new_parent2_right

    # student code end
    
    return offspring1, offspring2

#test
"""
test1 = []
for i in range(0, 8):
    test1.append(random.randint(1,8))
print(test1)

test2 = []
for i in range(0, 8):
    test2.append(random.randint(1,8))
print(test2)

off1, off2 = permutation_cut_and_crossfill(test1, test2)

print(off1)
print(off2)
"""