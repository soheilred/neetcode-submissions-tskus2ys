class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        minH = []

        for i in range(len(arr)):
            heapq.heappush(minH, (abs(arr[i] - x), i))
        
        res = []

        for j in range(k):
            res.append(arr[heapq.heappop(minH)[1]])
        
        res.sort()
        
        return res
        