from lock_helper import LockCombinationPuzzle
# веплюси
"""
In this assignment, you will interacted with a lock object as defined in the lock_helper.py file. 
Define a functionL: solve_lock_combination, which exhaustively generates the solution to unlock a sequence of combination locks.
You will need to read through the auxiliary file to understand how to interact with the lock-object.
"""
def solve_lock_combination(lock):
    # get keys lenght
    n = len(lock) 
    def backtrack(ring_index):
        # check if the current combination unlocks the lock.
        if lock.check_open():
            return True
        # when lenght is equal to n, it backtrack to the n-1 ring, which is the last ring, as the backtrack starts from 0.
        if ring_index == n:
            return False
        
        while True:
            # check if the combination is true. if somewhere deep in the backtrack we find the code it return true to main funciton.
            if backtrack(ring_index + 1):
                return True
            
            # if not true, the last ring rotates
            is_back_at_start = lock.turn_ring(ring_index)
            
            # if the most current ring is rotated to its initial position, go to the previous cycle.
            if is_back_at_start:
                break
        
        return False
    # backtrack start from 0 
    backtrack(0)
    
    """
    This function solves the lock with "n" rings problem.
    :param lock: The lock that needs to be opened.
    :type lock: lockRingPuzzle
    :return: This function does not have a return, as the lock object is changed.
    :rtype: None
    """
