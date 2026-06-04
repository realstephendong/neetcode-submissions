class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        

        # min(1 + dfs(amount - coins[i]))
        # if amount if 0, return 0

        def dfs(amount):
            if amount in cache: 
                return cache[amount]
            if amount == 0:
                return 0

            minCoins = float('inf')
            for coin in coins:
                if amount - coin >= 0:
                    curr = 1 + dfs(amount - coin)
                    minCoins = min(curr,minCoins)
                    
            cache[amount] = minCoins
            return minCoins
            
        ans = dfs(amount)
        if ans == float('inf'):
            return -1
        else:
            return ans