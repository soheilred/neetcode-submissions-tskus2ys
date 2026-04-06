class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n, m = len(matrix), len(matrix[0])

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    for k in range(n):
                        if matrix[k][j] != 0:
                            matrix[k][j] = '0'

                    for k in range(m):
                        if matrix[i][k] != 0:
                            matrix[i][k] = '0'
                    
                    # break
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '0':
                    matrix[i][j] = 0


        
        