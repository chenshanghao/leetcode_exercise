class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        if len(prices) < 2:
            return res
        low, high = prices[0], prices[1]
        res = max(res, high - low)
        for i in range(2, len(prices)):
            high = prices[i]
            low = min(low, prices[i - 1])
            res = max(res, high - low)
        return res    