class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2, n3 = len(s1), len(s2), len(s3)

        if n3 != n1 + n2: 
            return False
        
        def bt(s, r, k):
            print(s, r, k)
            if len(s) == 0:
                return k == n3 or r == s3[k:]
            
            if k == n3:
                return False

            if s[0] != s3[k]:
                return False

            i = 0
            while i < len(s) and i + k < n3 and s[i] == s3[k + i]:
                i += 1
            
            return bt(r, s[i:], k + i)
        
        return bt(s1, s2, 0) or bt(s2, s1, 0)

        