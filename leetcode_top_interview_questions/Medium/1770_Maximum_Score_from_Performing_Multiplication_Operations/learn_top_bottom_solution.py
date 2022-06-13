class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        # dp(i,j,m): max score give nums[i~j] and mul[m:]
        # base cases
        # dp(*, *, m) = 0 if m == M, all operations are used
        # Transition
        # dp(i, j, m) = max(
        # nums[i] * mul[m] + dp(i+1, j, m+1) use left
        # nums[j] * mul[m] + dp(i, j, m+1) use right
        #)
        
        n, m = len(nums), len(multipliers)
        memo = [[float('-inf')]* m for _ in range(m)]
        def dp(l, r):
            k = n - (r - l + 1)
            if k == m:
                return 0
            if memo[l][k] != float('-inf'): 
                return memo[l][k]
            memo[l][k] = max(dp(l + 1, r) + nums[l] * multipliers[k],
                       dp(l, r - 1) + nums[r] * multipliers[k])
            return memo[l][k]

        return dp(0, n - 1)
        