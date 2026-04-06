class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        n = len(nums)

        def bt(i, path):
            if len(path) > n:
                return

            res.append(path.copy())

            for j in range(i+1, n):
                path.append(nums[j])
                bt(j, path) 
                path.pop()
        bt(-1, [])
        return res
        