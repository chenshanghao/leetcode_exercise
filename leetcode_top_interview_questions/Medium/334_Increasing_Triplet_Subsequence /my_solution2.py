class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        i = 0
        j, k = -1, -1
        for n in range(1, len(nums)):
            if nums[n] > nums[i]:
                if j == -1:
                    j = n
                else:
                    if nums[n] > nums[j]:
                        return True
                    else:
                        j = n
            elif nums[n] < nums[i]:
                i = n
        return False
                        
                    