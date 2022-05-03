class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        len_nums = len(nums)
        if len_nums < 2:
            return len_nums
        l, r = 0, 1
        while r < len_nums:
            if nums[l] != nums[r]:
                nums[l + 1] = nums[r]
                l += 1
                r += 1
            else:
                r += 1
        return l + 1
            
        