class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        
        hashmap = {}
        res = 1
        
        for i in range(len(nums)):
            hashmap[i] = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    hashmap[i] = max(hashmap[i], hashmap[j] + 1)
            res = max(res, hashmap[i])
        
        return res
                