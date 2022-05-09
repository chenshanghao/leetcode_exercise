class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Solution 1: Brute force
        # Try every pair of walls
        # Time complexity: O(n^2)
        
        # Solution 2: 
        # Use two pointers (l, r) to describe a container
        # area = min(h[l], h[r]) * (r-l)
        
        # Start with l=0, r=n-1, the widest container
        # if h[l] < h[r]: ++l else: --r
        
        l, r = 0, len(height) - 1
        res = 0
        while l<r:
            res = max(min(height[l], height[r]) * (r - l), res)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return res