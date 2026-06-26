class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): 
            return -1
        
        tank = diff = start = 0

        for i in range(len(gas)):
            tank += gas[i]
            if tank >= cost[i]:
                tank -= cost[i]
            else:
                diff += cost[i] - tank
                start = i+1
                tank = 0
        
        if start == len(gas) or tank < diff:
            return -1
        
        return start