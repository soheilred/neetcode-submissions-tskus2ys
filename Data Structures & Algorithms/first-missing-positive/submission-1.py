class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)

        # for i in range(len(nums)):
        #     if nums[i] > N or nums[i] < 1:
        #         continue
        #         # return nums[i]
        #     if nums[i] > 0:
        #         nums[nums[i] - 1] = nums[i]
            
        
        # for i in range(N):
        #     if nums[i] != i + 1:
        #         return i+1
        res = 0

        for n in nums:
            if n > 0:
                res |= (1 << (n - 1))
        
        n = 0
        # print(res)
        while res:
            if res & 1 == 0:
                return n + 1
            n += 1
            res = res >> 1 
        
        return n + 1


            

        