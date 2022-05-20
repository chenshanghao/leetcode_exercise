class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        hashmap = {}
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if (i, j) in hashmap:
                    continue
                elif grid[i][j] == "0":
                    hashmap[i, j] = True
                else:
                    self.helper(i, j, m, n, grid, hashmap)
                    res += 1
        return res
    
    def helper(self, i, j, m, n, grid, hashmap):
        hashmap[i, j] = True
        grid[i][j] = "0"
        
        if i-1 >= 0 and grid[i-1][j] == "1":
            self.helper(i-1, j, m, n, grid, hashmap)
        
        if i + 1 < m and grid[i+1][j] == "1":
            self.helper(i+1, j, m, n, grid, hashmap)
        
        if j-1 >= 0 and grid[i][j-1] == "1":
            self.helper(i, j-1, m, n, grid, hashmap)
        
        if j+1 < n and grid[i][j+1] == "1":
            self.helper(i, j+1, m, n, grid, hashmap)
        
                    