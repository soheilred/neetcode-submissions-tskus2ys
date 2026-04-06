class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        # seen = set() # set of tupes of counts
        # res = []
        res = set()

        def dfs(combo, cur_sum):
            # print(combo, cur_sum)
            if cur_sum == target:
                combo.sort()
                res.add(tuple(combo))
                return
                
                # if combo not in seen:
                    # res.append(combo)
            if cur_sum < 0:
                return
            
            for num in nums:
                if cur_sum + num <= target:
                    combo.append(num)
                    dfs(combo.copy(), cur_sum + num)
                    combo.pop()
        
        dfs([], 0)
        return list([list(elem) for elem in res])
            
            
            


        