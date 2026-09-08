import numpy as np
from functools import cache
    
def bottom_up_shortest_edit_distance(a:str, b:str) -> int:
    """
    
    The goal is to turn the string A into the string B by a sequence of moves.
    There are three possible moves:
        1. Deletion: delete one letter from string A.
        2. Insertion: insert one letter into string A.
        3. Mutation: change one letter from A to a different one.
    This function returns the lowest possible number of moves to turn A into B.
    
    Do this by using bottom up dynamic programming.
    Hint: Solve the recurrence relation first. 
    What would be base case subproblems that you can solve without any smaller sub problems?
      
    :param A: The string that is to be modified into B.
    :type A: str
    :param B: The string that A must be modified into.
    :type B: str
    :return: The lowest possible amount of moves to modify A into B.
    :rtype: int
    """
    n = len(a)
    m = len(b)
    # 1. Създаваме матрицата
    dp = np.zeros((n + 1, m + 1), dtype=np.int64)
    # 2. Базови случаи
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j
    # 3. Попълване на матрицата
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # ВАЖНО: i и j в dp са с 1 по-големи от индексите в стринговете
            if a[i-1] == b[j-1]:
                # Буквите са еднакви - копираме стойноста от диагонала
                dp[i][j] = dp[i-1][j-1]
            else:
                # Буквите са различни - взимаме най-малкото от трите съседни + 1
                dp[i][j] = 1 + min(
                    dp[i-1][j],    # Deletion
                    dp[i][j-1],    # Insertion 
                    dp[i-1][j-1]  ) # Mutation
    return int(dp[n][m])
    raise NotImplementedError("Implement this function.")
