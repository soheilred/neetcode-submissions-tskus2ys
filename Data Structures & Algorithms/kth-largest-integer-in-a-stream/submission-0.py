class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = [-n for n in nums]
        heapq.heapify(self.heap)
        self.k = k
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, -val)
        # print(self.heap)
        rem = []
        for i in range(self.k):
            rem.append(heapq.heappop(self.heap))
        
        k_th = rem[-1]
        
        for i in range(self.k):
            rem.append(heapq.heappush(self.heap, rem[i]))

        return -k_th
        
