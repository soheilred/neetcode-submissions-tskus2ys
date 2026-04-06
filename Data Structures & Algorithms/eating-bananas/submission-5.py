class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        divisor = 1
        l, r = 1, max(piles)
        res = r

        while l <= r:
            hours = 0
            divisor = l + (r - l) // 2
            for i, p in enumerate(piles):
                # print(max(p // divisor, 1)+ int((bool(p % divisor))), end=' ')
                hours += p // divisor + int((bool(p % divisor)))

            # print(divisor, hours)
                    
            if hours <= h:
                res = divisor
                r = divisor - 1
            else:
                l = divisor + 1

            # divisor += 1

        return res