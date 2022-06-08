class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 2:
            return min(cost)
        
        dp0 = cost[0]
        dp1 = cost[1]
        
        for i in range(2, len(cost)):
            tmp = min(dp0, dp1) + cost[i]
            dp0 = dp1
            dp1 = tmp
        
        return min(dp0, dp1)
        