class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        res = -1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                res = mid
                break
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        if res == -1:
            return [-1, -1]
        l, r = res - 1, res + 1
        while l >= 0 and nums[l] == target:
            l -= 1

        while r < len(nums) and nums[r] == target:
            r += 1
        
        return [l+1, r-1]
                