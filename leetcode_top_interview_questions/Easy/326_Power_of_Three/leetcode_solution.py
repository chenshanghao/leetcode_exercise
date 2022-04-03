from math import log

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        else:
            cube_root = log(n)/log(3)
            cube_root_rounded = round(cube_root)
            diff = abs(cube_root - cube_root_rounded)
            return diff <= 1e-10
