class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        """
        >>> chr(97)
        'a'
        >>> ord('a')
        97
        """
        ans = 0
        for ch in columnTitle:
            ans = (ord(ch) - ord('A') + 1) + ans * 26
        return ans
            