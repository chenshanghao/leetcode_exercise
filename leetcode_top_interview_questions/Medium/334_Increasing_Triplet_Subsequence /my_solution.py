class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        i, j = -1, -1
        for idx in range(len(nums)):
            if i == -1:
                i = idx
            elif j == -1:
                if nums[idx] <= nums[i]:
                    i = idx
                else:
                    j = idx
            else:
                if nums[idx] > nums[j]:
                    return True
                elif nums[i] < nums[idx] <= nums[j]:
                    j = idx
                else:
                    i = idx
        return False
        