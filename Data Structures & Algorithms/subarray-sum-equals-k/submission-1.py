class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        N = len(nums)
        # pref = [0] * (N + 1)
        pref = {0: [-1]}
        cur = 0
        res = 0
        for i in range(N):
            cur += nums[i]

            if -k + cur in pref:
                res += len(pref[-k + cur])
                
            if cur in pref:
                pref[cur].append(i)
            else:
                pref[cur] = [i]
        
        
        return res
            
        