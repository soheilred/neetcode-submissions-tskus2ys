class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        # res = 0

        def bt(i, j):
            print(i, j)
            if j == m:
                return 1

            if i > n - (m -j):
                return 0
            
            if s[i] == t[j]:
                return bt(i+1, j+1) + bt(i+1, j)
            
            return bt(i+1, j)
        return bt(0, 0)
        # return res

        