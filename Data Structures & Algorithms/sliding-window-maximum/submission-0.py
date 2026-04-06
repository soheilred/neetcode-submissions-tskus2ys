class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        min_heap = [(-nums[i], i) for i in range(k-1)]
        heapq.heapify(min_heap)
        res = []
        # print(min_heap)

        for i in range(k-1, n):
            heapq.heappush(min_heap, (-nums[i], i))
            # print(i, min_heap)
            while i - min_heap[0][1] >= k:
                heapq.heappop(min_heap)
                # print(i, min_heap)
            res.append(-min_heap[0][0])
        
        return res


        