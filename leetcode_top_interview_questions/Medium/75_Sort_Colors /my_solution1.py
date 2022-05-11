class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red_cnt, white_cnt, blue_cnt = 0, 0, 0
        for num in nums:
            if num == 0:
                red_cnt += 1
            elif num == 1:
                white_cnt += 1
            else:
                blue_cnt += 1
        
        for i in range(len(nums)):
            if i < red_cnt:
                nums[i] = 0
            elif red_cnt <= i < red_cnt + white_cnt:
                nums[i] = 1
            else:
                nums[i] = 2
        