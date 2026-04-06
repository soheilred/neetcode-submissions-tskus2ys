class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        cur = 0

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            nums[cur] = nums[i]
            cur += 1
        return cur

        
'''
 nums = [1,1,2,3,4]
'''