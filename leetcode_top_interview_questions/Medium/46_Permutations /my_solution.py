class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.helper(nums, [], result)
        return result
    
    def helper(self, nums, tmp, result):
        if len(tmp) == len(nums):
            result.append(tmp[:])
            
        for num in nums:
            if num in tmp:
                continue
            self.helper(nums, tmp + [num], result)
