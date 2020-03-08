#by Ting Hu for COMP3201 A2

# compute fitness of an invidual for the 8-queen puzzle
def fitness_8queen (individual): # maximization
    M = 28
    check = 0
    # student code begin
    l = len(individual)
    for i in range (0, l):
        for j in range (i + 1, l):
            if abs(individual[i] - individual[j]) == abs(i-j) :
                check = check + 1

    # student code end
    return M - check


