class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found = set()
        
        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
            else:
                if triplet[0] == target[0]:
                    found.add(0)
                if triplet[1] == target[1]:
                    found.add(1)
                if triplet[2] == target[2]:
                    found.add(2)
        
        return len(found) == 3