class Solution:
    def isHappy(self, n: int) -> bool:
        val = 0
        seen = set()
        while val != 1 and val not in seen:
            seen.add(val)
            # print(val, n)
            val = 0
            while n > 0:
                val += (n % 10) ** 2
                n = n // 10
            n = val
            # print(val)
        
        # if val in seen:
            # return 
        if val == 1:
            return True
        return False
        