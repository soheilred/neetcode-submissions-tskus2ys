class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = 0
        for n in nums:
            if n == 0:
                zeros += 1

        if zeros > 1:
            return [0] * len(nums)
        
        pref = [1] * len(nums)
        suf = [1] * len(nums)

        for i in range(1, len(nums)):
            pref[i] = pref[i - 1] * nums[i - 1]

        
        for i in range(len(nums) - 1, 0, -1):
            suf[i - 1] = suf[i] * nums[i]
        
        print(pref, suf)

        return [pref[i] * suf[i] for i in range(len(nums))]