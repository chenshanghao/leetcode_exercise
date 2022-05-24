class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = 0
        expect_jump = len(nums) - 1
        for i, num in enumerate(nums):
            if i > max_jump:
                break
            else:
                max_jump = max(max_jump, i + nums[i])
            
            if max_jump >= expect_jump:
                return True
        
        return True if max_jump >= expect_jump else False
        