def rec_nQueens(size, queens=[]):
    # енфакториел
    """
    Recursively computes all solutions for the n-Queens puzzle.
    :param size: The size of the puzzle
    :type size: int
    :param queens: The currently placed queens, e.g. [4,2] represent
    that on row 0 there is a queen on the 4th index and on row 1 
    there is a queen on the 2nd index. 
    :type queens: list[int]
    
    :return: the (partial) list of queen posisitons
    :rtype: list[int]
    """
    # extra block for safety-management
    if queens is None:
        queens = []
    
    # return list of the poisitons when the lenght == size of the board
    if len(queens) == size:
        return [queens]
    all_result = []
    # for each column
    for col in range(size):
        # helper function
        if constraint(queens, col):
            # call the function with the new position added
            result = rec_nQueens(size, queens + [col])
            
            # if there is correct position, we add all the results to the previous cycle
            if result:
                all_result.extend(result)
    
    # otherwise, we return empty list and thus the previous cycle try to find another position for the queen
    return all_result
            
def constraint(queens, col):
    """
    The constraints for the n-queens problem.
    
    :param queens: The currently placed queens.
    :type queens: list[int]
    :param col: The column that the next queen would be placed
    :type col: int
    
    :return: If the puzzle constraint is satisfied or not
    :rtype: bool
    """
    # get the lenght of the current list
    new_row = len(queens)
    # check if current position of queen is instersected by previous positions
    for r, c in enumerate(queens):
        if c == col or abs(c-col) == abs(r - new_row):
            return False
    return True
