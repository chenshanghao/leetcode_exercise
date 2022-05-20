class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(nums, res, tmp, idx):
            res.append(tmp[::])
            for i in range(idx, len(nums)):
                tmp.append(nums[i])
                helper(nums, res, tmp, i+1)
                tmp.pop()
            return res
        
        res = helper(nums, [], [], 0)
        return res
            
        