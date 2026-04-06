class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        N = len(hand)
        if N % groupSize != 0: return False
        # hand.sort()
        rem = []
        heapq.heapify(hand)
        prev = hand[0] - 1
        gs = 0

        while hand:
            print(hand, rem)
            cur = heapq.heappop(hand)
            if cur - prev > 1:
                return False
            elif cur - prev == 1:
                prev = cur
                gs += 1
            else:
                rem.append(cur)
            
            if gs == groupSize:
                if len(rem) == 0 and len(hand) == 0:
                    return True

                gs = 0
                prev = rem[0] - 1 if rem else hand[0] - 1
                while rem:
                    heapq.heappush(hand, rem.pop())
        
        return gs == 0

         