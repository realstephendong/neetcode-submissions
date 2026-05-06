class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        bool_list = [False] * n
        temp = []
        ans = []

        def backtrack():
            if len(temp) == n:
                ans.append(temp.copy());
                return

            for i in range(n):
                if bool_list[i] == False:
                    temp.append(nums[i])
                    bool_list[i] = True
                    backtrack()
                    temp.pop()
                    bool_list[i] = False

        backtrack() 
        return ans
