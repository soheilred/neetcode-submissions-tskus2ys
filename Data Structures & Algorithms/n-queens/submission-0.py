class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]

        def safe(i, j):
            for k in range(n):
                if  board[i][k] == 'Q' or board[k][j] == 'Q':
                    return False
            
            # diagonal
            for (di, dj) in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
                new_i, new_j = i + di, j + dj 
                while -1 < new_i < n and -1 < new_j < n:
                    if board[new_i][new_j] == 'Q':
                        return False
                    new_i, new_j = new_i + di, new_j + dj 

            return True

        res = []
        def solve(row, i):
            nonlocal res
            if row == n:
                res.append([''.join(board[i]) for i in range(n)])
                return i == n - 1
            
            for j in range(n):
                if safe(row, j):
                    board[row][j] = 'Q'
                    solve(row+1, n + 1)
                    board[row][j] = '.'
            
            return False
        
        solve(0, 0)
        return res
        
'''
how to represent the board?
- criteria: optimized in detecting
    1. rows
    2. columns
    3. diagonal 
    4. off-diagonal

solver(row, col):
    1. check if it's the last column
        return if the last row and col is usable
    2. check if (row, col) is usable
        if not, traverse (row+1, j) j in (0, M)
    3. if usable, place at (row, col)
    4. proceed with (row+1, 0)
'''