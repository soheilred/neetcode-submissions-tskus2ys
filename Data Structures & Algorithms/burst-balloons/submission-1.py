class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        def dp(arr):
            if len(arr) - 2 == 1:
                return arr[1]
            
            res = 0
            for i in range(1, len(arr) - 1):
                cur = arr[i - 1] * arr[i] * arr[i + 1]
                # print(i, cur)
                res = max(res, cur + dp(arr[:i] + arr[i+1:]))
            
            return res
        
        return dp([1] + nums + [1])
            



        