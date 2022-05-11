class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Approach 1: Cascading
        # Time Complexity O(N * 2^N)
        # Space Complexity O(N * 2^N)
        n = len(nums)
        output = [[]]
        
        for num in nums:
            output += [curr + [num] for curr in output]
        return output        
        