class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        total = sum(nums)
        cur = 0

        for i,n in enumerate(nums):
            total -= n
        
            if cur == total:
                return i
                
            cur += n

        return -1
        