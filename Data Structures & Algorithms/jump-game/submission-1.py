class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = {}

        def bt(i):
            if i in memo:
                return memo[i]

            if i >= n - 1:
                memo[i] = True
                return True
            
            for j in range(1, nums[i]+1):
                if bt(i + j):
                    memo[i] = True
                    return True
                    
            memo[i] = False
            
            return False
        
        return bt(0)
        