class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        cache = {}

        def bt(i):
            if i > n - 1:
                return 0
            
            if i in cache:
                return cache[i]
            
            cache[i] = max(nums[i] + bt(i + 2), bt(i + 1))
            return cache[i]
        
        return bt(0)

        # def dp(house):
        #     if house > n - 1:
        #         cache[house] = 0
        #         return 0 
            
        #     if house in cache:
        #         return cache[house]
            
        #     cache[house] = max(nums[house] + dp(house + 2), dp(house + 1))
        #     return cache[house]
        
        # return dp(0)
        