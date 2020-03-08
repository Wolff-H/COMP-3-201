import random


"""
    定义一个关联数组函数
    把个体编号与其适应度对应起来
    返回一个数组i_and_fitness = [i,fitness]
"""
def toAssocArray(arr) :
    array = arr.copy()

    i_and_fitness = []

    # 创建数组 #
    for i in range( len(array) ):
        i_and_fitness.append( [i,array[i]] )

    print(i_and_fitness)

    return i_and_fitness

"""
    定义一个字典函数
    把个体编号与其适应度对应起来
    返回一个字典i_with_fitness = {i:fitness}
"""
def toDict(arr) :
    array = arr.copy()

    i_with_fitness = {}

    # 创建字典 #
    for i in range(len(array)):
        i_with_fitness[i] = array[i]

    print(i_with_fitness)

    return i_with_fitness


"""
    defined a cumulative distribution function for FPS
    定义一个cdf计算函数
    返回一个伪字典i_with_cp = [i,cdf]
"""
def calc_cdf(arr) :

    array = arr.copy()
    i_with_fitness = toDict(array)

    # 对字典按值排序，从大到小 #
    i_with_fitness = sorted(i_with_fitness.items(), key=lambda item: item[1], reverse=True)

    print("i_with_fitness", i_with_fitness)

    # 数列排序（大到小） #
    array.sort(reverse=True)

    # 计算数列的和 #
    array_sum = 0
    for item in array:
        array_sum = array_sum + item

    # 一个存分区的数列 #
    partitions = []
    for item in array:
        partitions.append(item / array_sum)

    # cumulative probabilities #
    cps = [0]
    for i in range( len(partitions) ) :
        cps.append(   cps[i]+partitions[i]   )

    # 替入字典 #
    i_with_cp = []
    for i in range( len(cps)-1 ) :
        i_with_cp.append(   [ i_with_fitness[i][0], cps[i+1] ]   )

    print("i_with_cp",i_with_cp)

    return i_with_cp








#multi-pointer selection (MPS)
def MPS(fitness, mating_pool_size):

    selected_to_mate = []    # list of the indices of picked parents

    #student code begin

    cdf = calc_cdf(fitness)
    # print(cdf)    # test
    print(fitness)

    size = mating_pool_size
    pool = []

    pointer = random.uniform( 0, 1/size )
    print(pointer)
    current = 0
    i = 0

    while current < size :
        while pointer <= cdf[i][1] :
            pool.append( cdf[i][0] )
            pointer = pointer + 1/size
            # print("ptr",pointer)
            current = current + 1
            # print("cur",current)
        i = i + 1

    print("pool",pool)

    selected_to_mate = pool

    #student code end

    return selected_to_mate




"""
    定义了一个选最佳函数
    返回一个名值对数组best = [i,order]
    i:该个体在fitness中的id号，order:该成员在打乱的i_and_fitness中的序号
"""
def raceBest(compete) :

    best_fit = 0
    best_id = 0
    order = 0
    for i in range( len(compete) ) :
        if compete[i][1] > best_fit :
            best_fit = compete[i][1]
            best_id = compete[i][0]
            order = i

    return [best_id,order]


#tournament selection without replacement
def tournament(fitness, mating_pool_size, tournament_size):

    selected_to_mate = []    # list of the indices of picked parents

    #student code begin

    print(tournament_size)
    print(mating_pool_size)

    # 创建关系数组 #
    i_and_fitness = toAssocArray(fitness)

    # 打乱 #
    random.shuffle(i_and_fitness)
    print(i_and_fitness)

    compete = []
    current = 0
    pool = []

    while current < mating_pool_size :
        for i in range(tournament_size) :
            compete.append(i_and_fitness[i])

        # print(compete)
        best = raceBest(compete)
        # print(best)
        pool.append(best[0])
        del i_and_fitness[best[1]]
        compete = []
        current = current + 1
        random.shuffle(i_and_fitness)
        # print(i_and_fitness)

    print(pool)
    selected_to_mate = pool


    #student code end

    return selected_to_mate


#randomly uniformly pick parents
def random_uniform (population_size, mating_pool_size):

    selected_to_mate = []    # list of the indices of picked parents

    #student code begin

    pop_ids = []
    for i in range( population_size ) :
        pop_ids.append(i)
    random.shuffle(pop_ids)

    selected_to_mate = pop_ids[0:mating_pool_size]

    #student code end

    return selected_to_mate
