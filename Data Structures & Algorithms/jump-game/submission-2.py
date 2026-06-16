class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True

        end = len(nums) - 1
        farthest = 0
        for i in range(len(nums)):
            if i > farthest:
                return False

            farthest = max(farthest, i + nums[i])
            
            if farthest >= end:
                return True

        return False