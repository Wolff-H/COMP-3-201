
import random

# initialize a population of permutation
def permutation (pop_size, chrom_length):
    
    population = []
    
    # student code begin
    """
        layout is an individual in population( population = all layouts )
        x,y is the coordinate of a chess piece
        y-coords are predefined as index in layout, i.e.
            layout = [a,b,c,d,e,f,g]
            y      =  1,2,3,4,5,6,7
        x-coords are those variables in layout as items, i.e.
            layout = [a,b,c,d,e,f,g]
            x      =  a,b,c,d,e,f,g
    """
    while len(population) < pop_size:
        layout = []
        while len(layout) < chrom_length:
            x = random.randint(1, 8)
            layout.append(x)
            if len(layout) == chrom_length:
                population.append(layout)
    
    # student code end
    
    return population



