class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r-l) // 2
            if nums[mid] == target:
                break
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        if nums[mid] != target:
            return [-1, -1]
        else:
            ldx, rdx = mid, mid
            while ldx >= 0:
                if nums[ldx] == target:
                    ldx -= 1
                else:
                    break
            
            while rdx < len(nums):
                if nums[rdx] == target:
                    rdx += 1
                else:
                    break
            return [ldx+1, rdx-1]
        