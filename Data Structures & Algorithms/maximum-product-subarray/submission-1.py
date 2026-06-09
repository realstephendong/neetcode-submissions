class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        if not nums:
            return nums[0]

        minimum = nums[0]
        maximum = nums[0]
        globalmax = maximum
        
        for i in range(1, len(nums)):
            case1 = nums[i]
            case2 = nums[i] * minimum
            case3 = nums[i] * maximum
            minimum = min(case1, case2, case3)
            maximum = max(case1, case2, case3)
            globalmax = max(globalmax, maximum)

        return globalmax