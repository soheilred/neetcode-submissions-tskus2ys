class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) == 0 or len(s2) == 0:
            return s1 == s3 or s2 == s3
        
        n, m = len(s1), len(s2)
        
        def bt(s, t, k):
            print(s, t, k)
            if len(s) == 0 and len(t) == 0 and k == len(s3):
                return True

            if k == len(s3):
                return False

            j = 0

            while j < len(s) and s[j] == s3[k+j]: 
                j += 1
            
            if j == 0:
                return False
            
            return bt(t, s[j:], k + j)
        
        return bt(s1, s2, 0) or bt(s2, s1, 0)

