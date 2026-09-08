def cut_rod(price):
    """
    Given a list of prices where price[i] is the price of a rod of length i+1,
    return the maximum price obtainable by cutting up the rod and selling the pieces.
    Use dynamic programming to speed up the solution.
    Use tabulation (bottom-up) or memoization (top-down) to solve this problem.
    
    Arguments:
    price -- List[int], where price[i] = price of rod length i+1
    Returns:
    int -- Maximum price obtainable
    """
    n = len(price)
    # list n+1, so [0] is base case
    dp = [0] * (n + 1)
    #start from 1, as it is minimum cutting lenght
    for i in range(1, n + 1):
        max_val = float("-inf")
        
        # check the options for each lenght
        for j in range(i):
    
            current_revenue = price[j] + dp[i - (j + 1)]
            
            # highest_price option for each lenght
            if current_revenue > max_val:
                max_val = current_revenue
        
        # save that option in the current index(lenght)
        dp[i] = max_val
    return dp[n]
