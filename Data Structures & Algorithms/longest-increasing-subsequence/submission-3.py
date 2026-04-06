class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        longest = 0

        def bt(cur, path):
            # print(cur, path)
            nonlocal longest
            # if cur == n - 1:
            longest = max(longest, len(path)) 
                # return
                
            if cur > n:
                return
            
            for i in range(cur+1, n):
                # print(i)
                if len(path) == 0 or nums[i] > path[-1]:
                    path.append(nums[i])
                    bt(i, path.copy())
                    path.pop()

        bt(-1, [])    
        return longest


            



'''
s = [0, ]
'''
        