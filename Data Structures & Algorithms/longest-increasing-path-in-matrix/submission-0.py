class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])

        memo = {}

        def dp(i, j):
            # if i in [0, n - 1] or j in [0, m - 1]:
                # memo[(i, j)] = 0
                # return 0

            if (i, j) in memo:
                return memo[(i, j)]
            
            res = 1
            
            # path.append((i, j))
            for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                i1, j1 = i + di, j + dj
                if -1 < i1 < n and -1 < j1 < m and matrix[i1][j1] > matrix[i][j]:
                    # path.append((i1, j1))
                    res = max(res, 1 + dp(i1, j1))
                    # path.pop()

            memo[(i, j)] = res
            
            return res
        
        for i in range(n):
            for j in range(m):
                dp(i, j)
        
        max_len = 0
        for i in range(n):
            for j in range(m):
                max_len = max(max_len, memo[(i, j)])
        print(memo)
        return max_len