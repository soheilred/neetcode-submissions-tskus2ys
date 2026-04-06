class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        candidates.sort()
        n = len(candidates)

        def dfs(start, combo, cur_sum):
            if cur_sum == target:
                res.append(combo)
                return
            
            if cur_sum > target:
                return
            
            for i in range(start, n):
                if i > start and candidates[i - 1] == candidates[i]:
                    continue
                    
                combo.append(candidates[i])
                dfs(i+1, combo.copy(), cur_sum + candidates[i])
                combo.pop()

        dfs(0, [], 0)
        return res
        