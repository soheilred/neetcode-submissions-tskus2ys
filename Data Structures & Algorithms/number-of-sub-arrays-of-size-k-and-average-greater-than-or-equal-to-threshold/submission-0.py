class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        total = sum(arr[:k])
        res = 0

        for i in range(k, n):
            if total / k >= threshold:
                res += 1
            total += arr[i] - arr[i-k]
        
        if total / k >= threshold:
            res += 1
        return res


        # def dfs(i, count, su):
        #     if count == k:
        #         if su // k >= threshold:
        #             return 1
        #         return 0

        #     res = 0
        #     for j in range(i+1, n):
        #         res += 
        