class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        hashmap = {}
        for coin in coins:
            hashmap[coin] = 1
            
        hashmap[0] = 0
        for i in range(1, amount + 1):
            if i in hashmap:
                continue
            hashmap[i] = float('inf')
            for coin in coins:
                if i - coin in hashmap:
                    hashmap[i] = min(hashmap[i], hashmap[i-coin] + 1)
        return hashmap[amount] if hashmap[amount] != float('inf') else -1