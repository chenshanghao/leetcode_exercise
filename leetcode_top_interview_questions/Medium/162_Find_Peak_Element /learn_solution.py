class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        start, end = 0, n-1
        while(start <= end):
            mid = start + (end-start)//2
            if (mid==0 or nums[mid]>nums[mid-1]) and (mid==n-1 or nums[mid]>nums[mid+1]):
                return mid
            elif(mid>0 and nums[mid-1]>nums[mid]):
                end = mid-1
            else:
                start = mid+1
        return mid