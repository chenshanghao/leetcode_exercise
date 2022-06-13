class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        # dp[i][k]  = min difficulty to schedule the first i jobs (1-based) in k days
        
        # Init
        # dp[0][0] = 0,
        # dp[*][*] = inf
        
        # Transition
        # dp[i][k] = min{dp[j][k-1] + max(jobs[k+1~i])}
        
        if d > len(jobDifficulty):
            return -1
        n = len(jobDifficulty)
        
        dp = [[float('inf') for _ in range(d + 1)]  for _ in range(n+1)]
        dp[0][0] = 0
        for i in range(1, n+1):
            for k in range(1,d+1):
                md = 0
                for j in range(i-1, k-2, -1):
                    md = max(md, jobDifficulty[j])
                    dp[i][k] = min(dp[i][k], dp[j][k-1] + md)
        return dp[n][d]