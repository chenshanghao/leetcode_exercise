class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # n = number of types of coins
        # m = desired amount
        # f[i][j] = the number of combinations to make up amount j with the first i types of coins
        # Induction rule
        # f[i][j] = sum(f[i-1][j],                // use coins[i-1] 0 times
        #               f[i-1][j-coins[i-1]],     // use coins[i-1] 1 times
        #               f[i-1][j-coins[i-1]*2]    // use coins[i-1] 2 times
        #                ..... )
        # More formally,
        # f[i][j] = sum(f[i-1][j-k*coins[i-1]], 0<=k<=j/coins[i-1])
        # Base case
        # f[0][0] = 1
        # f[0][1..m] = 0

        # More
        # f[i][j] = sum(f[i-1][j], f[i-1][j-coins[i-1]])
        
        if amount == 0:
            return 1
        n, m = len(coins) + 1, amount + 1
        dp = [[ 0 for j in range(m)] for i in range(n)]
        dp[0][0] = 1
        for j in range(1, m):
            dp[0][j] = 0
            
        for i in range(1, n):
            for j in range(m):
                dp[i][j] = dp[i-1][j]
                if j-coins[i-1] >= 0:
                    dp[i][j] = dp[i][j] + dp[i][j-coins[i-1]]
                    

        return dp[n-1][m-1]
        
        