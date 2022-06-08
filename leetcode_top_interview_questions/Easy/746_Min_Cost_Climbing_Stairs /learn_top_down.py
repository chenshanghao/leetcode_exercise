class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def minimum_cost(i):
            if i <= 1:
                return 0
            
            if i in hashmap:
                return hashmap[i]
            
            down_one = cost[i - 1] + minimum_cost(i - 1)
            down_two = cost[i - 2] + minimum_cost(i - 2)
            hashmap[i] = min(down_one, down_two)
            return hashmap[i]
        
        hashmap = {}
        return minimum_cost(len(cost))