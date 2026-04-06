class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        indic = 0

        for n in nums:
            print(bin(indic))
            if (indic >> n) & 1:
                return n
            indic ^= (1 << n)
        

        