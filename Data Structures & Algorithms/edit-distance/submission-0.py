class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        memo = {}
        n, m = len(word1), len(word2)

        def dp(i, j):
            print(i, j)
            if i == n:
                return m - j

            if j == m:
                return n - i
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            if word1[i] == word2[j]:
                return dp(i + 1, j + 1)

            res = 1 + min(dp(i + 1, j + 1), dp(i, j + 1), dp(i + 1, j))
            
            memo[(i, j)] = res
            return res
        
        return dp(0, 0)

        