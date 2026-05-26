class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}

        def dfs(step):
            if step >= len(nums):
                return 0
            
            if step in cache:
                return cache[step]
            else:
                money = max(nums[step] + dfs(step+2), dfs(step+1))
                cache[step] = money
                return money

        return max(dfs(0), dfs(1))
        # money = max(nums(i) + dfs(i+2), dfs(i+1))

