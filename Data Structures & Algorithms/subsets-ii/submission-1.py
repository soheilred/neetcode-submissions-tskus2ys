class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()
        seen = [False] * n

        # def solve(start, seen, combo):
        def solve(start, combo):
            if len(combo) > n:
                return
            
            res.append(combo)

            for i in range(start, n):
                # if seen[i] or i > start and nums[i-1] == nums[i]:
                if i > start and nums[i-1] == nums[i]:
                    continue
                # seen[i] = True
                combo.append(nums[i])
                # solve(i+1, seen, combo.copy())
                solve(i+1, combo.copy())
                combo.pop()
                # seen[i] = False
            
        # solve(0, seen, [])
        solve(0, [])
        return res

        