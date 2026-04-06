class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        if n < m:
            text1, text2 = text2, text1
            n, m = m, n

        memo = {}

        def bt(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            # if i == n - 1 or j == m - 1: 
            #     memo[(i, j)] = 1 if i == n - 1 and j == m - 1 else 0
            #     return memo[(i, j)]
            
            if i >= n or j >= m:
                memo[(i, j)] = 0
                return 0
            
            if text1[i] == text2[j]:
                memo[(i, j)] = 1 + bt(i + 1, j + 1)
                return memo[(i, j)]

            memo[(i, j)] = max(bt(i+1, j), bt(i, j+1))
            return memo[(i, j)]
        bt(0,0)
        print(memo)
        return max(memo.values())

            
        