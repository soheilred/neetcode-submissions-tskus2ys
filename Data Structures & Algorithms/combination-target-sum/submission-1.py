class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        # seen = set() # set of tupes of counts
        # res = []
        res = []
        n = len(nums)

        def dfs(start, combo, cur_sum):
            # print(combo, cur_sum)
            if cur_sum == target:
                res.append(combo)
                return
                
                # if combo not in seen:
                    # res.append(combo)
            if cur_sum < 0:
                return
            
            for i in range(start, n):
                if cur_sum + nums[i] <= target:
                    combo.append(nums[i])
                    dfs(i, combo.copy(), cur_sum + nums[i])
                    combo.pop()
        
        dfs(0, [], 0)
        # return list([list(elem) for elem in res])
        return res
            
            
            


        