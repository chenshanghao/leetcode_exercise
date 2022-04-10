class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        left, right, length = 0, len(s) - 1, len(s)
        while(left < right):
            while(left < length):
                if s[left].isalnum() :
                    break
                else:
                    left += 1
            
            while(right >= 0):
                if s[right].isalnum() :
                    break
                else:
                    right -= 1
            
            if left == length or right == -1:
                break
            
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
            
        return True