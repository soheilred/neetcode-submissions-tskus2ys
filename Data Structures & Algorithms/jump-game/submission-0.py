class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        def bt(i):
            print(i)
            if i >= n - 1:
                return True
            
            for j in range(1, nums[i]+1):
                if bt(i + j):
                    return True
            
            return False
        
        return bt(0)
        