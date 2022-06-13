class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        dp = [[0 for i in range(n)] for j in range(m)]
        res = 0
        for i in range(m):
            dp[i][0] = int(matrix[i][0])
            res = max(dp[i][0], res)
        
        for j in range(n):
            dp[0][j] = int(matrix[0][j])
            res = max(dp[0][j], res)
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    res = max(res, dp[i][j])
                else:
                    dp[i][j] = 0
        
        return res*res
                
        