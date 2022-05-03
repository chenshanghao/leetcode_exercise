class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_val = float('-inf')
        last_max_val = float('-inf')
        for num in nums:
            max_val = max(max_val, num, last_max_val + num)
            last_max_val = max(num, last_max_val + num, 0)
        return max_val