class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_num_index = dict()
        length = len(nums)
        for i in range(length):
            remaining = target - nums[i]
            if remaining in dict_num_index:
                return [dict_num_index[remaining], i]
            else:
                dict_num_index[nums[i]] = i