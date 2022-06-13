class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            dp[coin] = 1
        
        for i in range(1, amount+1):
            if dp[i] == 1:
                continue
            for coin in coins:
                dp[i] = min(dp[i], dp[i-coin] + 1)
                
        return dp[amount] if dp[amount] != float('inf') else -1
            