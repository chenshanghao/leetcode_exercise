class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
# row 1: 0
# row 2: 01
# row 3: 0110
# row 4: 01101001
# We see that, for any level N, the first half of the string is the same as the string in N-1, the next #half is just complement of it. The total number of items in level N is 2^N. The half mark of the #string is marked by [2^(N-1)]-th item. So, for any level N:

# if K is in the first half, it is same as the Kth element in level N-1
# if K is in the second half, it is the complement of the number in [K-2^(N-1)]-th position in level N-#1

        if n == 1:
            return 0

        half = pow(2, n-2)
        if k <= half:
            return self.kthGrammar(n-1, k)
        else:
            res = self.kthGrammar(n-1, k-half)
            return 0 if res == 1 else 1
            
        