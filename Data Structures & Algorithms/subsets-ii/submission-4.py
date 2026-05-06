class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        temp = []
        ans = []
        n = len(nums)

        def backtrack(i, curr_subset):
            if i == len(nums):
                ans.append(temp.copy())
                return
            curr_subset.append(nums[i])
            backtrack(i+1, curr_subset)
            curr_subset.pop()

            while i + 1 < n and nums[i] == nums[i+1]:
                i += 1
            backtrack(i+1, curr_subset)

        backtrack(0, temp)
        return ans