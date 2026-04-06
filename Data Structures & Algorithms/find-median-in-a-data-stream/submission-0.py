class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []
        self.median = 0
        

    def addNum(self, num: int) -> None:
        # if len(self.left) > 0:
        max_left = -self.left[0] if len(self.left) > 0 else float('inf')
        min_right = self.right[0] if len(self.right) > 0 else float('inf')
        if num < max_left:
            heapq.heappush(self.left, -num)
        else:
            heapq.heappush(self.right, num)
        
        if abs(len(self.left) - len(self.right)) > 1:
            if len(self.left) > len(self.right):
                heapq.heappush(self.right, -heapq.heappop(self.left))
            else:
                heapq.heappush(self.left, -heapq.heappop(self.right))
        
        print("left", self.left, "right", self.right)
        

    def findMedian(self) -> float:
        # print(len(self.right) + len(self.left) % 2)
        if (len(self.right) + len(self.left)) % 2 == 1:
            # print(-self.left[0] if len(self.left) > len(self.right) else self.right[0])
            return -self.left[0] if len(self.left) > len(self.right) else self.right[0]
        else:
            return (-self.left[0] + self.right[0]) / 2
        
        