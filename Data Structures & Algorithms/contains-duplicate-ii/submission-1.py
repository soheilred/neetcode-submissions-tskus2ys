class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        positions = {}

        for i, n in enumerate(nums):
            if n in positions:
                positions[n].append(i)
            else:
                positions[n] = [i]
        
        for p in positions:
            if len(positions[p]) < 2:
                continue
            
            for i in range(len(positions[p])):
                for j in range(i+1, len(positions[p])):
                    if abs(positions[p][j] - positions[p][i]) <= k:
                        # print(positions[p][i], positions[p][j])
                        return True

        
        return False
        