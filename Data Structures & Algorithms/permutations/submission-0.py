class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums)
        n = len(nums)
        res = []

        def solve(combo, counter):
            if len(combo) == n:
                res.append(combo)
                return
            
            if len(combo) > n:
                return
            
            for i in range(n):
                if counter[nums[i]] <= 0:
                    continue
                counter[nums[i]] -= 1
                combo.append(nums[i])
                solve(combo.copy(), counter)
                combo.pop()
                counter[nums[i]] += 1
        
        solve([], count)
        return res
        