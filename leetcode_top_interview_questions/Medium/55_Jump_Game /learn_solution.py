class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_position = 0
        for i, num in enumerate(nums):
            last_position = max(last_position, i + num)
            if last_position >= len(nums) - 1:
                return True
            if last_position == i:
                break
        return False
        
        
            