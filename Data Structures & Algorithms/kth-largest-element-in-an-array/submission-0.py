class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [n for n in nums]
        heapq.heapify(heap)

        while len(heap) > k:
            heapq.heappop(heap)
        
        return heap[0]
        
        
        