class StockSpanner:

    def __init__(self):
        self.prices = []
        

    def next(self, price: int) -> int:
        self.prices.append(price)
        
        N = len(self.prices)
        # for i in range(N):
        back = 1
        while N > back and self.prices[N - 1 - back] <= price:
            back += 1
            # res.append(res + 1)
        return back
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

'''
prices = [100, 80, 60, 70, 60, 75, 85]
[1, 1, 1, 2, 1, 4, 6]
minH

BF:
N = len(nums)
for i in range(N):
    back = 0
    while i > back and prices[i - back] < price[i]:
        back -= 1
    res.append(res + 1)

    

'''