class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()

        def two_sum(arr, target):
            l, r = 0, len(arr) - 1

            while l < r:
                if arr[l] + arr[r] == target:
                    if len(res) == 0 or (res[-1][0] != arr[l] or res[-1][1] != arr[r]):
                        res.append([arr[l], arr[r], -target])
                    l += 1
                    r -= 1
                
                elif arr[l] + arr[r] < target:
                    l += 1
                
                else:
                    r -= 1
        
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                two_sum(nums[i+1:], -nums[i])
        
        return res


'''
nums = [-1,0,1,2,-1,-4]
nums = [-4, -1, -1, 0, 1, 2]
'''
        