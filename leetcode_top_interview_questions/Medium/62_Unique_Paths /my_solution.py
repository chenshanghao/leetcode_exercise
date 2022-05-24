class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # nums[i][j] == nums[i-1][j] + nums[i][j-1]
        nums = [[0 for i in range(n)] for j in range(m)]
        nums[0][0] = 1
        for i in range(1, m):
            nums[i][0] = 1
        for j in range(1, n):
            nums[0][j] = 1
            
        for i in range(1, m):
            for j in range(1, n):
                nums[i][j] = nums[i-1][j] + nums[i][j-1]
        return nums[m-1][n-1]