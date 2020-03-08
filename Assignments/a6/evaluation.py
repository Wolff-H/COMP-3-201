import numpy

# compute fitness of an individual for the 8-queen puzzle
# here var individual is the one layout


def fitness_8queen(individual):    # maximization
    
    M = 28
    check = 0
    
    # student code begin

    # below defined some helper functions ##########################################################

    """
        sum an arithmetic progression
    """
    def sumAP(n) :
        sum = (n+1)*n/2
        return sum
    
    """
        convert a layout(array) to a matrix
    """
    def layoutToMatrix(layout) :
        matrix = []
        size = len(layout)
        for x in layout :
            row = [0]*size
            row[x-1] = x
            matrix.append(row)
        return matrix

    """
        print the matrix out so it's cognitive
        (for test only)
    """
    def printMatrix(matrix) :
        for row in matrix :
            print(row)

    """
        calculate checked behind a num(y,x) in matrix
        checked = non-zero numbers behind num in the diagonals where the num is
                = [...no-need...num...checked...]  for diagonal and back-diagonal
    """
    def calcCheckBehind(np_matrix, size, y, x) :
        
        k = x - y    # offset magnitude of diagonal
        bkk = (size+1-x) - y    # offset magnitude of back-diagonal
        diagonal = numpy.diag(np_matrix, k)
        bkdiagonal = numpy.diag( numpy.fliplr(np_matrix), bkk )

        # calculate amount of non-zero numbers behind x for diag #
        checked_diag = 0
        behind = False
        for num in diagonal :
            if num != 0 and behind == True :
                checked_diag = checked_diag + 1
            if num != 0 and num == x :
                behind = True
        
        # calculate amount of non-zero numbers behind x for back-diag #
        checked_bkdiag = 0
        bkbehind = False
        for num in bkdiagonal :
            if num != 0 and bkbehind == True :
                checked_bkdiag = checked_bkdiag + 1
            if num != 0 and num == x :
                bkbehind = True

        # calculate amount of checks
        checks_diag = sumAP(checked_diag)
        checks_bkdiag = sumAP(checked_bkdiag)

        return checks_diag + checks_bkdiag
            
    # below starts mechanism #######################################################################

    """
        known y-coords are predefined
        inspect how many checks occur in a layout in case
            chess pieces plot on the same x-coord (behind current one)
    """
    check_on_x = 0
    x_with_repeat = {}
    for x in individual :
        if x not in x_with_repeat.keys() :
            x_with_repeat[x] = 0
        else :
            x_with_repeat[x] = x_with_repeat[x] + 1

    for repeat in x_with_repeat.values() :
        check_on_x = check_on_x + sumAP(repeat)
    
    """
        inspect how many checks occur in a layout in case
            chess pieces plot on the diagonal (behind current one)
    """
    check_diagonals = 0

    matrix = layoutToMatrix(individual)

    np_matrix = numpy.array(matrix)    # convert to numpy ndarray(matrix)

    for i in range( len(individual) ) :
        check_diagonals = check_diagonals + calcCheckBehind(np_matrix, len(individual), i+1, individual[i])

    check = check_on_x + check_diagonals

    # student code end
    
    return M - check
