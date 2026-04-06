class Solution:
    def solve(self, board: List[List[str]]) -> None:

        n,m = len(board), len(board[0])
        seen = [[False] * m for _ in range(n)]

        def dfs(i, j):
            if -1 < i < n and -1 < j < m and board[i][j] == 'O':
                board[i][j] = 'T'
                dfs(i + 1, j)
                dfs(i - 1, j)
                dfs(i, j + 1)
                dfs(i, j - 1)
        
        for i in range(n):
            dfs(i, 0)
            dfs(i, m - 1)
        
        for i in range(m):
            dfs(0, i)
            dfs(n - 1, i)
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

                if board[i][j] == 'T':
                    board[i][j] = "O"

        