class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0

        for n in nums:
            res = res | (1 << n)
        
        # print(res)
        
        count = 0
        while res:
            bit = res & 1
            if bit == 0:
                return count
            count += 1
            res = res >> 1
        
        return count

        