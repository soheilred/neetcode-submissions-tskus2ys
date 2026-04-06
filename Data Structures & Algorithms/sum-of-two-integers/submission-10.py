class Solution:
    def getSum(self, a: int, b: int) -> int:
        if b > a:
            a, b = b, a
        mask = (1 << 16) - 1
        max_int = (1 << 15) - 1

        while b != 0:
            a, b = (a ^ b) & mask, (a & b) & mask
            b = (b << 1) & mask
        return a if a <= max_int else ~(a ^ mask)
            

