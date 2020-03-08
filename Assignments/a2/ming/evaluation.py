import random

def calculateHorizontalPairs(individual):
    """
    A function to calculate the pairs in a permutation
    :param n: amount of the number
    :return: amount of pairs
    """
    result = 0
    if n < 2:
        return 0
    if n == 2:
        return 1
    while n > 0:
        result = result + (n - 1)
        n = n - 1
    return result

# compute fitness of an invidual for the 8-queen puzzle
def fitness_8queen (individual): # maximization
    
    M = 28
    check = 0
    
    # student code begin
    #count the horizontal alleles in chromosome
    count = [0]*len(individual) + [0]*10
    for i in range(1, 9):
        for j in range(len(individual)):
            if individual[j] == i:
                count[i] += 1

    #check the same alleles in horizontal
    for i in range(len(count)):
        temp = calculateHorizontalPairs(count[i])
        check += temp

    



    # student code end
    
    return M - check


#test
"""
test = []
for i in range(0, 8):
    test.append(random.randint(1,8))
print(test)

fitness_8queen(test)
"""