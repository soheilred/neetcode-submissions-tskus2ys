class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        N, M = len(matrix), len(matrix[0])
        self.pref_sum = [[0] * (M+1) for _ in range(N+1)]
        for i in range(N):
            for j in range(M):
                self.pref_sum[i+1][j+1] = self.pref_sum[i][j+1] + self.pref_sum[i+1][j] - self.pref_sum[i][j] + matrix[i][j]
        
        print(self.pref_sum)
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # print(self.pref_sum[row2+1][col2+1], self.pref_sum[row1][col2], self.pref_sum[row2][col1], self.pref_sum[row1][col1])
        return self.pref_sum[row2+1][col2+1] - self.pref_sum[row1][col2+1] - self.pref_sum[row2+1][col1] + self.pref_sum[row1][col1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

'''
[2, 3, 5, 1, 4, 9]
pref_sum = [2, 5, 10, 11, 15, 24]
pref_sum[j] - pref_sum[i]
pref_sum[i][j] = -pref_sum[i - 1][j - 1] + pref_sum[i][j - 1] + pref_sum[i - 1][j] + nums[i][j]
[3, 0, 1, 4, 2], 
[5, 6, 3, 2, 1], 
[1, 2, 0, 1, 5], 
[4, 1, 0, 1, 7], 
[1, 0, 3, 0, 5]]]

[0, 0, 0, 0, 0, 0], 
[0, 3, 3, 4, 8, 10], 
[0, 8, 14, 18, 24, 27], 
[0, 9, 17, 21, 28, 36], 
[0, 13, 22, 26, 34, 49], 
[0, 14, 23, 30, 38, 58]]

'''