class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        xt, yt, zt = target
        found = [0] * 3
        for t in triplets:
            if t[0] > xt or t[1] > yt or t[2] > zt:
                continue
            for i in range(3):
                if t[i] == target[i]:
                    found[i] = 1
        
        return sum(found) == 3
            
            
        