class Solution:
    def myPow(self, x, n):
        
        #Deal with negative power:
        if n < 0: 
            x = 1/x
            n = abs(n)
            
        #Iterate:
        res = 1
        while n:
            if n % 2:
                res = res*x
            x = x*x 
            n = n//2
            
        return res