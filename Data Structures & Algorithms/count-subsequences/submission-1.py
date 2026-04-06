class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        cache = {}
        # res = 0

        def bt(i, j):
            if (i,j) in cache:
                return cache[(i, j)]

            if j == m:
                cache[(i, j)] = 1
                return 1

            if i > n - (m -j):
                cache[(i, j)] = 0
                return 0
            
            if s[i] == t[j]:
                cache[(i, j)] = bt(i+1, j+1) + bt(i+1, j)
                return cache[(i, j)]
            
            return bt(i+1, j)
        return bt(0, 0)
        # return res

        