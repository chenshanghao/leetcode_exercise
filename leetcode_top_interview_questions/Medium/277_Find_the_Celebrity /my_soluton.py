# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        celebrity_candiate = 0
        for i in range(1, n):
            if knows(celebrity_candiate, i):
                celebrity_candiate = i
                
        for i in range(n):
            if i == celebrity_candiate:
                continue
            if knows(celebrity_candiate, i) or not knows(i, celebrity_candiate):
                return -1
        return celebrity_candiate
        