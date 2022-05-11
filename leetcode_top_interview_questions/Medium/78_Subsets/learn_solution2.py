class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Backtracking
        # Time complexity: O(N * 2^N)
        # Space complexity O(N)
        self.result = []
        self.helper(0, sorted(nums), [])
        return self.result
    
    def helper(self, start, s, temp):
        self.result.append(temp[:])
        for i in range(start, len(s)):
            temp.append(s[i])
            self.helper(i+1, s, temp)
            temp.pop()