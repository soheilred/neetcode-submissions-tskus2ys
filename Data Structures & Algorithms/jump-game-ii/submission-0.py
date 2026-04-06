class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        def bt(i):
            # print(i)
            if i >= n - 1:
                return 0
            
            end = min(n - i, nums[i])
            res = float('inf')
            for j in range(end, 0, -1):
                print(end, j)
                res = min(1 + bt(i + j), res)
            
            return res
        
        return bt(0)
        