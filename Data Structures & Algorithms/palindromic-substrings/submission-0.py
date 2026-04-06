class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = []

        def isPal(i, j):
            l, r = i, j

            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            
            return True
        
            
        for i in range(n):
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
                res.append(s[l:r+1])
            
            l, r = i, i+1
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
                res.append(s[l:r+1])
                
        return len(res)


        