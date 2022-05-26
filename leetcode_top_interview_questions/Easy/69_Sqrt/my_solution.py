class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        l, r = 1, x // 2
        while l <= r:
            mid = l + (r-l)//2
            if mid*mid <= x < (mid+1)*(mid+1):
                return mid
            elif mid*mid < x:
                l = mid + 1
            else:
                r = mid -1