def maze_solver(maze):
    # веплюси
    """
    Starting in the top left corner (0,0) determine whether there is a path,
    moving horizontally and vertically, to exit the labyrinth in the bottom-right corner.

    :param maze: A 2D list representing a maze, with 0 for paths and 1 for walls
    :type maze: list[list[int]]
    :return: True/False whether there is a way to exit the labyrinth
    """
    # each row represent item from the outer list
    rows = len(maze)
    # the columns equal to the values inside the list
    columns = len(maze[0])

    def backtrack(r, c):
        # False if path out of matrix
        if r < 0 or r >= rows: return False
        if c < 0 or c >= columns: return False
        # or path hit obstacle
        if maze[r][c] != 0: return False

        # True if we end up the bottom-right corner
        if r == rows - 1 and c == columns - 1: return True

        # mark the positions we already visit to neglect cycle walking
        maze[r][c] = 2

        # it backtrack the function to its all 4 neighbours
        if (backtrack(r - 1, c) or
            backtrack(r + 1, c) or
            backtrack(r, c - 1) or
            backtrack(r, c + 1)):
            return True

        # return False if neither of the paths are the right one
        return False

    # call the backtrac from the starting position
    return backtrack(0, 0)
