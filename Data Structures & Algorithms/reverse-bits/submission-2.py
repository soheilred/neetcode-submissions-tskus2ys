class Solution:
    def reverseBits(self, n: int) -> int:
        val = 0

        # while n:
        for i in range(31):
            val = val | ((n >> i) & 1)
            # print(val, n>>i, (n >> i) & 1)
            val <<= 1
        val = val | ((n >> 31) & 1)
        
        return val
        