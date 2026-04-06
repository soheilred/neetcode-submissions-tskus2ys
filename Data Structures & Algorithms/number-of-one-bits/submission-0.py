class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n > 0:
            rem = n % 2
            n = n >> 1
            if rem > 0:
                count += 1
        
        return count

        