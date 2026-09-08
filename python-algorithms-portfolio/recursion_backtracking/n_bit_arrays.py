def n_bitArr(n):
    # двенан-тастепен
    """
    Implement a function that returns a (list of) every list of 0's and 1's of length n 
    (in any order)
    For example, n_bitArr(1) -> [[0],[1]]
    For example, n_bitArr(2) -> [[0,0],[0,1],[1,0],[1,1]]  
    :return: A list containing all lists of 1's 0's of length n 
    :rtype: list[list[int]]
    """     
    result = []
    def backtrack(current_list):
        # if lenght of the variation matches with (n), we add a copy of it in result and return to previous backtrack
        if len(current_list) == n:
            result.append(current_list[:])
            return
        
        # Explore the branch where the next bit is 0
        current_list.append(0)
        backtrack(current_list)
        current_list.pop() # pop to try next backtrack
        # Explore the branch where the next bit is 1
        current_list.append(1)
        backtrack(current_list)
        current_list.pop() # pop to try previous backtrack
       
    backtrack([])
    
    return result
