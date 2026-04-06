class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        nums.sort()

        def two_sum(i):
            target = -nums[i]
            l, r = i + 1, n - 1

            while l < r:
                if nums[l] + nums[r] == target:
                    if len(res) == 0 or (res[-1][0] != nums[l] or res[-1][1] != nums[r]):
                        res.append([nums[l], nums[r], -target])
                    l += 1
                    r -= 1
                
                elif nums[l] + nums[r] < target:
                    l += 1
                
                else:
                    r -= 1
        
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                two_sum(i)
        
        return res


'''
nums = [-1,0,1,2,-1,-4]
nums = [-4, -1, -1, 0, 1, 2]
'''
        