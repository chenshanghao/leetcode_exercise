class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Time Complexity: O(N^2)
        # Space Complexity: O(logN)
        nums = sorted(nums)
        res = []
        # corner case
        if len(nums) <= 2:
            return res
        
        for i in range(0, len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            target = 0 - nums[i]
            l, r = i+1, len(nums) -1
            while l < r:
                while l > i+1 and nums[l] == nums[l-1] and l < r:
                    l += 1
                    
                while r < len(nums) -1 and nums[r] == nums[r+1] and r >l:
                    r -= 1
                    
                if l == r:
                    break
                
                if nums[l] + nums[r] == target:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1
        return res
            
        