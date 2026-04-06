class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        res = []

        def dfs(start, combo):
            if len(combo) > n:
                return
            
            res.append(combo)

            for i in range(start+1, n):
                combo.append(nums[i])
                dfs(i, combo.copy())
                combo.pop()
            
        dfs(-1, [])
        return res
        