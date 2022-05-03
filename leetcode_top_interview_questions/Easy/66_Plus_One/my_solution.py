class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        idx = len(digits) - 1
        while True:
            if idx < 0:
                digits.insert(0, 1)
                break
            val = digits[idx] + 1
            if val == 10:
                digits[idx] = 0
                idx -= 1
            else:
                digits[idx] = val
                break
        return digits