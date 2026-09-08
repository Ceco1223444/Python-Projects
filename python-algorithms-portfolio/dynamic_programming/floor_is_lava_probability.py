def floor_is_lava(grid, position, final_position, n, dp):
    """
    Calculates the probability of reaching the final_position from the given position
    in exactly n steps, moving only to adjacent (up, down, left, right) non-lava cells.
    Parameters:
    -----------
    grid : List[List[int]]
        A 2D list representing the map. A value of 1 indicates a safe cell,
        and 0 indicates a lava cell that cannot be stepped on.
    position : Tuple[int, int]
        The starting coordinates (x, y) in the grid.
    final_position : Tuple[int, int]
        The target coordinates (fx, fy) in the grid to reach in exactly n steps.
    n : int
        The exact number of steps allowed to reach the final position.
    dp : dict
        A memoization dictionary to cache subproblem results for optimization.
        Keys are tuples of the form (x, y, steps_remaining), and values are 
        computed probabilities for those states.
    Returns:
    --------
    float
        The probability of reaching the final_position from position in exactly n steps,
        moving only to adjacent safe cells with equal probability in each direction.
    Notes:
    ------
    - If a move would go out of bounds or onto lava, it contributes 0 to the probability.
    - At each step, the function tries all four directions (up/down/left/right) with equal probability (0.25).
    - If n == 0, the function returns 1.0 only if the current position is the final position,
      otherwise returns 0.0.
    """
    
    # unpack the tuples
    x, y = position
    fx ,fy = final_position
    rows = len(grid)
    cols = len(grid[0])
    # return 0, if out of boundaries or hit a lava
    if x < 0 or x >= rows or y < 0 or y >= cols or grid[x][y] == 0:
        return float(0)
    # when no steps left
    if n==0:
        # return 1, if position is final_position
        if x == fx and y == fy:
            return float(1)
        # return 0 otherwise
        else:
            return float(0)
    # save current step in tuple
    state = (x, y, n)
    # if the step is calculated return it
    if state in dp:
        return dp[state]
    
    total_probability = 0
    directions = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    # for each of the 4 direcitons
    for next_step in directions:
        # sum the probability for every position from the current step
        total_probability += floor_is_lava(grid, next_step, final_position, n - 1, dp)
    
    # divide it to estimate the chance for the current step
    result = total_probability * 0.25
    # save it
    dp[state] = result
    return result
    raise NotImplementedError('To do')
