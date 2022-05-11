class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.helper(nums, [], res)
        return res
        
    
    def helper(self, nums, tmp, res):
        res.append(tmp[:])
        for num in nums:
            if num in tmp:
                continue
            if len(tmp) > 0 and tmp[-1] > num:
                continue
            tmp.append(num)
            self.helper(nums, tmp, res)
            tmp.pop()
        
        