class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def helper(coins, reminder, tmp, idx, res):
            if reminder == 0:
                res.append(tmp[:])
                return
            elif reminder < 0:
                return
            else:      
                for i in range(idx, len(coins)):
                    tmp.append(coins[i])
                    helper(coins, reminder-coins[i], tmp, i, res)
                    tmp.pop()
            return res
        res = []
        helper(coins, amount, [], 0, res)
        return len(res)
        
        