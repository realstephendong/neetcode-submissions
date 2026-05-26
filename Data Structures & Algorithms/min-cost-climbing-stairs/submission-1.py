class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        n = len(cost)

        def dfs(step):
            if step >= n:
                return 0
            
            if step in cache:
                return cache[step]
            else:
                stepcost = cost[step] + min(dfs(step + 1), dfs(step + 2))
                cache[step] = stepcost
                return stepcost
            
        
        cost0 = dfs(0)
        cost1 = dfs(1)

        return min(cost0, cost1)

            
