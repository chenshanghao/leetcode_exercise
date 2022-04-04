class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum_nums = sum(nums)
        expect_sum = sum([i for i in range(len(nums) + 1)])
        missing_num = expect_sum - sum_nums
        return missing_num