import numpy as np
def bus_schedule_problem(price_matrix):
    """
    We are given a price matrix with the cost of traveling between bus stops.
    The first bus stop is always 0 and the last bus stop is always n-1.
    The cost of traveling from bus stop i to bus stop j is given by price_matrix[i][j].
    The cost of traveling from bus stop i to bus stop j is 0 if i == j.
    The goal is to find the minimum cost to travel from the first bus stop to the last bus stop.
    Example:
    [[0, 5, 10, 15],
     [0, 0, 7, 13],
     [0, 0, 0, 4],
     [0, 0, 0, 0]]
    The minimum cost to travel from bus stop 0 to bus stop 3 is 14 (stop 0 -> stop 2 -> stop 3).
    This function calculates the minimum cost to travel from the first bus stop to the last bus stop using dynamic programming.
    :param price_matrix: A matrix representing the cost of traveling between bus stops, where price_matrix[i][j] 
    is the cost to travel from bus stop i to bus stop j.
    :return: The minimum cost to travel from the first bus stop to the last bus stop
    :rtype: int
    """
    #bottom-up approach as we start from the first stop and store the next values in a list
    # time complexity = n^2, because the 2 for cycles (everything else is basic operations - =, +, -, etc.)
    # get the number of bus-stops
    n = len(price_matrix)
    # store the min price for each bus-stop
    min_cost = [float("inf")] * n
    # set the first one to 0
    min_cost[0] = 0
    for j in range(1,n):
        
        # for every bus-stop before stop[j]
        for i in range(j):
            # check the price
            path_from_i_to_j = min_cost[i] + price_matrix[i][j]
            # store price if its lower than the previous one
            if path_from_i_to_j < min_cost[j]:
                min_cost[j] = path_from_i_to_j
    # return lowest price for the last stop
    return(min_cost[n-1])
