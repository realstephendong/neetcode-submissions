class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        current_end = 0
        farthest = 0
        steps = 0
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            if i == current_end:
                steps += 1
                current_end = farthest
            
                if current_end > len(nums) - 1:
                    return steps
        
        return steps