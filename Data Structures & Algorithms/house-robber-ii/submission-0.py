class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        
        nums0 = nums[:len(nums)-1]
        nums1 = nums[1:]
        def dfs(step, num, cache):
            if step >= len(num):
                return 0
            
            if step in cache:
                return cache[step]
            else:
                money = max(num[step] + dfs(step + 2, num, cache), dfs(step + 1, num, cache))
                cache[step] = money
                return money
        
        return max(dfs(0, nums0, {}), dfs(0, nums1, {}))
