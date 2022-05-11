class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        # formats range in the requested format
        # Time Complexity O(N)
        # Space Complexity O(1)
        def formatRange(lower, upper):
            if lower == upper:
                return str(lower)
            else:
                return str(lower) + "->" + str(upper)
        
        result = []
        prev = lower - 1
        for i in range(len(nums) + 1):
            curr = nums[i] if i < len(nums) else upper + 1
            if prev + 1 <= curr - 1:
                result.append(formatRange(prev + 1, curr - 1))
            prev = curr
        return result