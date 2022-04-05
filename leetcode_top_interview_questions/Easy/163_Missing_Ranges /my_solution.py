class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
                
        def getRanges(ranges, left, right):
            if right - left <= 1:
                pass
            elif right - left == 2:
                ranges.append(str(left + 1))
            else:
                ranges.append(str(left+1) + "->" + str(right-1))
            return ranges
        
        nums_length = len(nums)
        ans = []
        if nums_length == 0:
            ans = getRanges(ans, lower-1, upper+1)
            return ans
        
        ans = getRanges(ans, lower-1, nums[0])
        for i in range(nums_length-1):
            ans = getRanges(ans, nums[i], nums[i+1])
        ans = getRanges(ans, nums[-1], upper+1)
        return ans

        