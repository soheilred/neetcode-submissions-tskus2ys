class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [(-(x[0] ** 2 + x[1] ** 2), x) for x in points]
        heapq.heapify(heap)
        while len(heap) > k:
            heapq.heappop(heap)
        
        return [h[1] for h in heap]

        