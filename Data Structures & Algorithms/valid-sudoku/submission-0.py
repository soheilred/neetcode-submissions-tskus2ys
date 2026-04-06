class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = [set() for i in range(9)]
        block = [set() for i in range(9)]
        for i in range(9):
            row = set()
            for j in range(9):
                if board[i][j] != '.':
                    # check each row
                    if board[i][j] in row:
                        return False
                    row.add(board[i][j])
                
                    # check column
                    if board[i][j] in columns[j]:
                        return False
                    columns[j].add(board[i][j])
    
                    # check block
                    b_i, b_j = i // 3, j // 3
                    if board[i][j] in block[b_i * 3 + b_j]:
                        return False
                    block[b_i * 3 + b_j].add(board[i][j])
        return True
                    
        