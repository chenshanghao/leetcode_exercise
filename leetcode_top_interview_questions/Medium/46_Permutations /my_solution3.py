class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(nums, tmp, res):
            if len(tmp) == len(nums):
                res.append(tmp[:])
                return
            for num in nums:
                if num in tmp:
                    continue
                tmp.append(num)
                helper(nums, tmp, res)
                tmp.pop()
        res = []
        helper(nums, [], res)
        return res
                
