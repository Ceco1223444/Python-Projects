import sys
from functools import cache

def shortest_edit_distance(A: str, B: str) -> int:
    """

    The goal is to turn the string A into the string B by a sequence of moves.
    There are three possible moves:
    1. Deletion: delete one letter from string A.
    2. Insertion: insert one letter into string A.
    3. Mutation: change one letter from A to a different one.
    This function returns the lowest possible number of moves to turn A into B.

    Do this by using dynamic programming.

    Hint: Complete the Least Common Subsequence problem first.

    Hint: Solve the recurrence relation first.
    What would be the subproblems and what variables would you need.



    :param A: The string that is to be modified into B.
    :type A: str
    :param B: The string that A must be modified into.
    :type B: str
    :return: The lowest possible amount of moves to modify A into B.
    :rtype: int
    """

    @cache
    def solve(i, j):
        # Базови случаи:
        if i == 0: return j  # Ако А е празна, добавяме всички букви от B
        if j == 0: return i  # Ако B е празна, трием всички букви от A

        # Ако текущите букви са еднакви, няма цена (0)
        if A[i-1] == B[j-1]:
            return solve(i-1, j-1)

        # Ако са различни, избираме най-евтиния от 3-те варианта:
        return 1 + min(
            solve(i-1, j),    # Deletion
            solve(i, j-1),    # Insertion
            solve(i-1, j-1)   # Mutation
        )

    return solve(len(A), len(B))
