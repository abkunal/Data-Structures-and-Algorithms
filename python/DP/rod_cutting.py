""" Given a rod of length n and list of prices of rod of length i where 1 <= i <= n, 
    find the optimal way to cut rod into smaller rods in order to maximize profit. """

def rod_cut(n, prices):
    # base case
    if n == 0:
        return 0
    # use a dictionary to remember pre-computed values
    memo = {i:0 for i in range(n+1)}
    
    # try every possible combination of cutting the rod
    for i in range(1, n+1):
        for j in range(1, i+1):
            memo[i] = max(memo[i], prices[j-1] + memo[i-j])
    return memo[n]


prices = [1,5,8,9,10,17,17,20]
print(rod_cut(8, prices))
