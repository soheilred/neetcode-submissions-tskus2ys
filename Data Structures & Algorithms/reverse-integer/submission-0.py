class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        sign = 1
        if x < 0:
            sign *= -1
            x *= -1

        while x and -2**32 < res < 2 ** 31 - 1:
            res += x % 10
            x = x // 10
            if x == 0:
                return sign * res

            res *= 10
        
        if not -2**32 < res < 2 ** 31 - 1:
            return 0
        
        return res * sign

        