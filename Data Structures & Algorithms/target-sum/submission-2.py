class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        memo = {}
        
        def bt(i, rem):
            print(i, rem)
            if rem == 0 and i == n:
                memo[(i, rem)] = 1
                return 1
            
            if i >= n:
                return 0
            
            if (i, rem) in memo:
                return memo[(i, rem)]
            
            res = 0
            # if nums[i] <= rem:
            res = bt(i + 1, rem - nums[i]) + bt(i + 1, rem + nums[i])
            
            memo[(i, rem)] = res
            return res
        
        return bt(0, target)
            
