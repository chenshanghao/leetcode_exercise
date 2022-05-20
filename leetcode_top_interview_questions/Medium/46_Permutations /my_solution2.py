class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(nums, res, tmp):
            if len(tmp) == len(nums):
                res.append(tmp[::])  
            for num in nums:
                if num not in tmp:
                    tmp.append(num)
                    helper(nums, res, tmp)
                    tmp.pop()
            return res
                    
        res = helper(nums, [], [])
        return res
                
