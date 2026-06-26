class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        freq = Counter(hand)

        hand.sort()
        
        for i in range(len(hand)):
            if freq[hand[i]] == 0:
                continue
            else:
                for num in range(hand[i], hand[i] + groupSize):
                    if freq[num] == 0:
                        return False
                    else:
                        freq[num] -= 1
        
        return True
